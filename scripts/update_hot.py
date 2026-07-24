# -*- coding: utf-8 -*-
"""
抖音热榜抓取脚本（免Key，公开接口）
输出: workbench/data/hot_data.js  -> window.HOT_DATA = {...}
用法: python update_hot.py
"""
import json
import os
import sys
import datetime
import urllib.request

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_JS = os.path.join(BASE, "data", "hot_data.js")
OUT_RAW = os.path.join(BASE, "data", "raw_hot.json")

API = ("https://www.douyin.com/aweme/v1/web/hot/search/list/"
       "?device_platform=webapp&aid=6383&channel=channel_pc_web")

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"),
    "Referer": "https://www.douyin.com/",
}

LABEL_MAP = {1: "新", 3: "热", 5: "首发", 8: "独家"}


def fetch():
    req = urllib.request.Request(API, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    data = fetch()
    word_list = data.get("data", {}).get("word_list", [])
    if not word_list:
        print("ERROR: word_list 为空，接口可能变更", file=sys.stderr)
        sys.exit(1)

    items = []
    for i, w in enumerate(word_list, 1):
        word = w.get("word", "")
        items.append({
            "rank": i,
            "word": word,
            "hot": round(w.get("hot_value", 0) / 10000, 1),  # 单位: w
            "label": LABEL_MAP.get(w.get("label", 0), ""),
            "url": "https://www.douyin.com/search/" + urllib.request.quote(word),
        })

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    payload = {"updatedAt": now, "hotList": items}

    os.makedirs(os.path.dirname(OUT_JS), exist_ok=True)
    with open(OUT_RAW, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    with open(OUT_JS, "w", encoding="utf-8") as f:
        f.write("window.HOT_DATA = ")
        f.write(json.dumps(payload, ensure_ascii=False, indent=2))
        f.write(";\n")

    print(f"OK: {len(items)} 条热榜已写入 {OUT_JS} ({now})")


if __name__ == "__main__":
    main()

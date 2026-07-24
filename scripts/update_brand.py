# -*- coding: utf-8 -*-
import json, os

base = r'C:\Users\Admin\WorkBuddy\2026-07-23-23-28-01\workbench'

# ---------- 1. index.html ----------
html_path = os.path.join(base, 'index.html')
h = open(html_path, encoding='utf-8').read()
repl = {
    '<meta name="theme-color" content="#5a7d24">':
        '<meta name="theme-color" content="#FFC300">',
    '<title>图书带货工作台</title>':
        '<title>老王日志</title>',
    '  --green:#5a7d24;--green-light:#eaf0d8;--green-border:#c9dba3;':
        '  --green:#FFC300;--green-light:#FFF6D6;--green-border:#FFE08A;',
    '.nav-item.active{background:var(--green);color:#fff;font-weight:600;box-shadow:inset 0 0 0 1px rgba(90,125,36,.15)}':
        '.nav-item.active{background:var(--green);color:#222;font-weight:700;box-shadow:inset 0 0 0 1px rgba(180,134,11,.25)}',
    '.sync-btn{display:inline-flex;align-items:center;gap:5px;padding:6px 14px;border:1px solid var(--green);border-radius:99px;background:var(--green-light);color:var(--green);font-size:12.5px;font-weight:600;cursor:pointer;transition:.15s}':
        '.sync-btn{display:inline-flex;align-items:center;gap:5px;padding:6px 14px;border:1px solid var(--green);border-radius:99px;background:var(--green-light);color:#222;font-size:12.5px;font-weight:600;cursor:pointer;transition:.15s}',
    '.install-btn{display:inline-flex;align-items:center;gap:5px;padding:6px 14px;border:none;border-radius:99px;background:var(--green);color:#fff;font-size:12.5px;font-weight:600;cursor:pointer;transition:.15s}':
        '.install-btn{display:inline-flex;align-items:center;gap:5px;padding:6px 14px;border:none;border-radius:99px;background:var(--green);color:#222;font-size:12.5px;font-weight:600;cursor:pointer;transition:.15s}',
    '#pwa-install{position:fixed;top:0;left:0;right:0;background:#5a7d24;color:#fff;padding:10px 16px;display:flex;align-items:center;justify-content:space-between;z-index:9999;font-size:13.5px;box-shadow:0 2px 8px rgba(0,0,0,.15)}':
        '#pwa-install{position:fixed;top:0;left:0;right:0;background:var(--green);color:#222;padding:10px 16px;display:flex;align-items:center;justify-content:space-between;z-index:9999;font-size:13.5px;box-shadow:0 2px 8px rgba(0,0,0,.15)}',
    '.plan-input button{border:none;background:var(--green);color:#fff;border-radius:10px;padding:0 18px;font-size:14px;font-weight:600;cursor:pointer;white-space:nowrap}':
        '.plan-input button{border:none;background:var(--green);color:#222;border-radius:10px;padding:0 18px;font-size:14px;font-weight:600;cursor:pointer;white-space:nowrap}',
    '.memo-save-btn{display:inline-flex;align-items:center;gap:6px;margin-top:10px;padding:8px 24px;border:none;background:var(--green);color:#fff;border-radius:99px;font-size:14px;font-weight:600;cursor:pointer}':
        '.memo-save-btn{display:inline-flex;align-items:center;gap:6px;margin-top:10px;padding:8px 24px;border:none;background:var(--green);color:#222;border-radius:99px;font-size:14px;font-weight:600;cursor:pointer}',
    '      <div class="name" id="userName">图书带货博主</div>':
        '      <div class="name" id="userName">老王</div>',
    '      <div class="role">创作工作台</div>':
        '      <div class="role">每日创作日志</div>',
    "function syncStatus(msg,ok){const s=$('syncState');if(s){s.textContent=msg;s.style.color=ok===false?'#df4446':ok?'#5a7d24':'#999';}}":
        "function syncStatus(msg,ok){const s=$('syncState');if(s){s.textContent=msg;s.style.color=ok===false?'#df4446':ok?'#e0a800':'#999';}}",
    'banner.innerHTML=\'<span>📱 安装到手机桌面，可全屏独立运行</span><button onclick="installApp()" style="background:#fff;color:#5a7d24;border:none;padding:6px 16px;border-radius:99px;font-weight:600;cursor:pointer;white-space:nowrap">立即安装</button>\';':
        'banner.innerHTML=\'<span>📱 安装到手机桌面，可全屏独立运行</span><button onclick="installApp()" style="background:#222;color:#FFC300;border:none;padding:6px 16px;border-radius:99px;font-weight:600;cursor:pointer;white-space:nowrap">立即安装</button>\';',
}
for old, new in repl.items():
    c = h.count(old)
    if c != 1:
        print(f'WARN count={c} for: {old[:40]}')
    h = h.replace(old, new)
open(html_path, 'w', encoding='utf-8').write(h)
print('index.html updated')

# ---------- 2. manifest.json ----------
mp = os.path.join(base, 'manifest.json')
m = json.load(open(mp, encoding='utf-8'))
m['name'] = '老王日志'
m['short_name'] = '老王日志'
m['description'] = '老王日志 · 每日任务管理 + 抖音爆款二创灵感'
m['theme_color'] = '#FFC300'
json.dump(m, open(mp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('manifest.json updated')

# ---------- 3. strings.xml ----------
sp = os.path.join(base, 'android/app/src/main/res/values/strings.xml')
s = open(sp, encoding='utf-8').read()
s = s.replace('<string name="app_name">图书带货工作台</string>', '<string name="app_name">老王日志</string>')
s = s.replace('<string name="title_activity_main">图书带货工作台</string>', '<string name="title_activity_main">老王日志</string>')
open(sp, 'w', encoding='utf-8').write(s)
print('strings.xml updated')

# ---------- 4. capacitor.config.json ----------
cp = os.path.join(base, 'capacitor.config.json')
c = json.load(open(cp, encoding='utf-8'))
c['appName'] = '老王日志'
json.dump(c, open(cp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('capacitor.config.json updated')

# ---------- 5. ic_launcher_background.xml ----------
bp = os.path.join(base, 'android/app/src/main/res/values/ic_launcher_background.xml')
b = open(bp, encoding='utf-8').read().replace('#5a7d24', '#FFC300')
open(bp, 'w', encoding='utf-8').write(b)
print('ic_launcher_background.xml updated')

print('ALL BRAND UPDATES DONE')

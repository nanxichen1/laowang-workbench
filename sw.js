/* Service Worker - 图书带货工作台 PWA */
const CACHE = 'wb-v3';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './data/hot_data.js',
  './data/inspiration.js',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-1024.png'
];

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(c => {
      // 逐个缓存，单个失败不影响整体（保证SW能成功安装）
      return Promise.allSettled(ASSETS.map(u => c.add(u).catch(() => {})));
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  // 仅处理同源请求
  if (url.origin !== location.origin) return;

  // network-first：优先拉取最新资源，失败再回退缓存（保证更新即时生效，不被旧缓存卡住）
  e.respondWith(
    fetch(e.request).then(res => {
      if (res && res.ok && res.type === 'basic') {
        const clone = res.clone();
        caches.open(CACHE).then(c => c.put(e.request, clone));
      }
      return res;
    }).catch(() => {
      return caches.match(e.request).then(cached => cached || caches.match('./index.html'));
    })
  );
});

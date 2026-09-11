// ARTUS site.js — nav state, mobile menu, scroll reveal (no dependencies)
(function () {
  var nav = document.querySelector('.nav');
  var onScroll = function () { nav.classList.toggle('scrolled', window.scrollY > 24); };
  onScroll(); window.addEventListener('scroll', onScroll, { passive: true });

  var burger = document.querySelector('.burger');
  if (burger) {
    burger.addEventListener('click', function () {
      var open = document.body.classList.toggle('menu-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('.nav-links a').forEach(function (a) {
      a.addEventListener('click', function () { document.body.classList.remove('menu-open'); });
    });
  }

  var here = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(function (a) {
    if (a.getAttribute('href') === here) a.classList.add('active');
  });

  var els = document.querySelectorAll('.rv');
  // 첫 화면 안에 있는 요소는 관찰을 기다리지 않고 바로 드러낸다 (첫 페인트 공백 방지)
  var vh = window.innerHeight || 800;
  els.forEach(function (el) { if (el.getBoundingClientRect().top < vh * 0.95) el.classList.add('in'); });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  // count-up for .count elements (data-to, data-suffix)
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return; co.unobserve(e.target);
        var el = e.target, to = parseFloat(el.getAttribute('data-count')), dec = (el.getAttribute('data-dec') | 0), t0 = null;
        var step = function (ts) {
          if (!t0) t0 = ts; var p = Math.min(1, (ts - t0) / 1400); p = 1 - Math.pow(1 - p, 3);
          el.textContent = (to * p).toFixed(dec); if (p < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { co.observe(el); });
  }
})();

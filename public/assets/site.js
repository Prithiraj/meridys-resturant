/* Everything essential works without JavaScript. This only refines navigation. */
(() => {
  'use strict';
  const navigation = document.querySelector('.mobile-navigation');
  if (navigation instanceof HTMLDetailsElement) {
    const summary = navigation.querySelector('summary');
    navigation.addEventListener('click', event => {
      if (event.target instanceof Element && event.target.closest('a')) {
        navigation.open = false;
      }
    });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && navigation.open) {
        navigation.open = false;
        summary?.focus();
      }
    });
    document.addEventListener('click', event => {
      if (navigation.open && event.target instanceof Node && !navigation.contains(event.target)) {
        navigation.open = false;
      }
    });
    const desktop = window.matchMedia('(min-width: 1024px)');
    desktop.addEventListener('change', event => {
      if (event.matches) navigation.open = false;
    });
  }

  // Highlight the currently visible menu section without hiding or filtering content.
  const menuLinks = Array.from(document.querySelectorAll('.menu-jump-nav a'));
  if ('IntersectionObserver' in window && menuLinks.length) {
    const linksBySection = new Map(menuLinks.map(link => [link.hash.slice(1), link]));
    const observer = new IntersectionObserver(entries => {
      const visible = entries.filter(entry => entry.isIntersecting)
        .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (!visible) return;
      menuLinks.forEach(link => link.removeAttribute('aria-current'));
      linksBySection.get(visible.target.id)?.setAttribute('aria-current', 'location');
    }, { rootMargin: '-15% 0px -50% 0px', threshold: [0, 0.15, 0.5] });
    linksBySection.forEach((link, id) => {
      const section = document.getElementById(id);
      if (section) observer.observe(section);
    });
  }
})();

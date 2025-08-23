const hamburger = document.getElementById("hamburger");
// static/js/sidebar.js
document.addEventListener('DOMContentLoaded', () => {
  const hamburger = document.getElementById('hamburger');
  const sidebar   = document.getElementById('sidebar');
  const body      = document.body;

  function toggle(open) {
    const willOpen = open ?? !body.classList.contains('sidebar-open');
    body.classList.toggle('sidebar-open', willOpen);
    // swap icon: ☰ ↔ X
    hamburger.innerHTML = willOpen ? '&#10005;' : '&#9776;';
    hamburger.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
  }

  // Toggle via hamburger
  hamburger.addEventListener('click', (e) => {
    e.stopPropagation();
    toggle();
  });

  // Close when clicking outside
  document.addEventListener('click', (e) => {
    if (!body.classList.contains('sidebar-open')) return;
    if (sidebar.contains(e.target) || hamburger.contains(e.target)) return;
    toggle(false);
  });

  // Close with ESC
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && body.classList.contains('sidebar-open')) {
      toggle(false);
    }
  });
});

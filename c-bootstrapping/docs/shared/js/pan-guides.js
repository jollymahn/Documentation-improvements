/* ══════════════════════════════════════════════════════════════════
   PAN Implementation Guides — Shared JavaScript
   Copy buttons, scroll spy, back-to-top, mobile sidebar

   Usage: <script src="../../shared/js/pan-guides.js"></script>
   ══════════════════════════════════════════════════════════════════ */

// Copy-to-clipboard for code blocks
function copyCode(btn) {
  const code = btn.previousElementSibling.querySelector('code') || btn.previousElementSibling;
  navigator.clipboard.writeText(code.textContent).then(() => {
    btn.textContent = 'Copied!';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.textContent = 'Copy';
      btn.classList.remove('copied');
    }, 2000);
  });
}

// Scroll spy for sidebar active section
const sections = document.querySelectorAll('h2[id]');
const sidebarLinks = document.querySelectorAll('.sidebar a[data-section]');

function updateActiveSection() {
  let current = '';
  sections.forEach(section => {
    if (section.getBoundingClientRect().top <= 120) {
      current = section.id;
    }
  });
  sidebarLinks.forEach(link => {
    link.classList.toggle('active', link.dataset.section === current);
  });
}

// Back-to-top button
const backToTop = document.getElementById('backToTop');
function updateBackToTop() {
  if (backToTop) {
    backToTop.classList.toggle('visible', window.scrollY > 400);
  }
}

// Close mobile sidebar on link click
sidebarLinks.forEach(link => {
  link.addEventListener('click', () => {
    const sidebar = document.querySelector('.sidebar');
    if (sidebar) sidebar.classList.remove('open');
  });
});

// Collapsible sections
document.querySelectorAll('.collapsible-header').forEach(header => {
  header.addEventListener('click', () => {
    header.classList.toggle('open');
    const body = header.nextElementSibling;
    if (body) body.classList.toggle('open');
  });
});

// Combined scroll handler
window.addEventListener('scroll', () => {
  updateActiveSection();
  updateBackToTop();
}, { passive: true });

// Initial state
updateActiveSection();

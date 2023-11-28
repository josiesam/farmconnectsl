const mobileMenu2Toggle = document.getElementById('mobile-menu-2-toggle');
const toggleMobileMenuHamburger = document.getElementById('toggle-mobile-menu-hamburger');
const toggleMobileMenuClose = document.getElementById('toggle-mobile-menu-close');

mobileMenu2Toggle.addEventListener('click', () => {
    toggleMobileMenuHamburger.classList.toggle('hidden')
    toggleMobileMenuClose.classList.toggle('hidden')
})
document.addEventListener('DOMContentLoaded', () => {
    console.log('Portfolio V2 Loaded');

    // Optional: Add smooth scrolling if not handling via CSS
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});

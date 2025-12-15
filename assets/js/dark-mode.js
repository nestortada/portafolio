// Dark Mode Functionality
document.addEventListener('DOMContentLoaded', function () {
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;
    const icon = darkModeToggle.querySelector('i');

    // Check for saved dark mode preference or default to light mode
    const currentTheme = localStorage.getItem('theme') || 'light';

    // Apply the saved theme
    if (currentTheme === 'dark') {
        body.setAttribute('data-theme', 'dark');
        body.classList.add('dark-mode');
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
        darkModeToggle.setAttribute('title', 'Cambiar a modo claro');
    }

    // Toggle dark mode
    darkModeToggle.addEventListener('click', function () {
        const currentTheme = body.getAttribute('data-theme');

        if (currentTheme === 'dark') {
            // Switch to light mode
            body.removeAttribute('data-theme');
            body.classList.remove('dark-mode');
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
            darkModeToggle.setAttribute('title', 'Cambiar a modo oscuro');
            localStorage.setItem('theme', 'light');
        } else {
            // Switch to dark mode
            body.setAttribute('data-theme', 'dark');
            body.classList.add('dark-mode');
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
            darkModeToggle.setAttribute('title', 'Cambiar a modo claro');
            localStorage.setItem('theme', 'dark');
        }
    });
});

// Enhanced carousel functionality for mobile responsiveness
document.addEventListener('DOMContentLoaded', function () {
    const carousel = document.querySelector('#carouselExampleCaptions');

    if (carousel) {
        // Add touch support for better mobile experience
        let touchStartX = 0;
        let touchEndX = 0;

        carousel.addEventListener('touchstart', function (e) {
            touchStartX = e.changedTouches[0].screenX;
        });

        carousel.addEventListener('touchend', function (e) {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        });

        function handleSwipe() {
            const swipeThreshold = 50;
            const swipeDistance = touchEndX - touchStartX;

            if (Math.abs(swipeDistance) > swipeThreshold) {
                const carouselInstance = bootstrap.Carousel.getInstance(carousel);

                if (swipeDistance > 0) {
                    // Swipe right - go to previous slide
                    carouselInstance.prev();
                } else {
                    // Swipe left - go to next slide
                    carouselInstance.next();
                }
            }
        }

        // Pause carousel on hover for better UX
        carousel.addEventListener('mouseenter', function () {
            const carouselInstance = bootstrap.Carousel.getInstance(carousel);
            if (carouselInstance) {
                carouselInstance.pause();
            }
        });

        carousel.addEventListener('mouseleave', function () {
            const carouselInstance = bootstrap.Carousel.getInstance(carousel);
            if (carouselInstance) {
                carouselInstance.cycle();
            }
        });
    }
});

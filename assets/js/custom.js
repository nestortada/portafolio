/**
 * custom.js - JavaScript personalizado para el portafolio
 * 
 * Este archivo contiene funciones para mejorar la experiencia del usuario
 * con animaciones, interactividad y funcionalidades responsive.
 */

document.addEventListener('DOMContentLoaded', function() {
    // Inicializar animaciones de scroll
    initScrollAnimations();
    
    // Mejorar interactividad de las tarjetas
    enhanceCardInteractivity();
    
    // Mejorar la navegación móvil
    enhanceMobileNavigation();
    
    // Mejorar modales
    enhanceModals();
});

/**
 * Inicializa animaciones basadas en scroll
 */
function initScrollAnimations() {
    // Detectar elementos que deben animarse al hacer scroll
    const animatedElements = document.querySelectorAll('.post, .mini-post, .blurb, .posts article');
    
    // Configurar el observador de intersección para animar elementos cuando son visibles
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1
    });
    
    // Observar todos los elementos animados
    animatedElements.forEach(el => {
        observer.observe(el);
    });
}

/**
 * Mejora la interactividad de las tarjetas de proyectos
 */
function enhanceCardInteractivity() {
    // Añadir efecto de elevación a las tarjetas al pasar el mouse
    const cards = document.querySelectorAll('.post, .mini-post');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 10px 20px rgba(0,0,0,0.1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 5px 15px rgba(0,0,0,0.1)';
        });
    });
}

/**
 * Mejora la navegación en dispositivos móviles
 */
function enhanceMobileNavigation() {
    // Asegurarse de que el menú móvil sea fácil de usar
    const menuToggle = document.querySelector('.menu a');
    const menu = document.getElementById('menu');
    
    if (menuToggle && menu) {
        // Cerrar el menú al hacer clic en un enlace dentro del menú
        const menuLinks = menu.querySelectorAll('a');
        menuLinks.forEach(link => {
            link.addEventListener('click', function() {
                menu.classList.remove('visible');
            });
        });
    }
}

/**
 * Mejora la experiencia de usuario con los modales
 */
function enhanceModals() {
    // Cerrar modales al hacer clic fuera del contenido
    const modals = document.querySelectorAll('.modal');
    
    modals.forEach(modal => {
        modal.addEventListener('click', function(e) {
            // Si se hace clic en el fondo del modal (no en su contenido)
            if (e.target === modal) {
                modal.classList.remove('active');
                
                // Pausar videos si existen en el modal
                const videos = modal.querySelectorAll('video');
                videos.forEach(video => {
                    video.pause();
                    video.currentTime = 0;
                });
            }
        });
    });
    
    // Cerrar modales con la tecla Escape
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            modals.forEach(modal => {
                if (modal.classList.contains('active')) {
                    modal.classList.remove('active');
                    
                    // Pausar videos si existen en el modal
                    const videos = modal.querySelectorAll('video');
                    videos.forEach(video => {
                        video.pause();
                        video.currentTime = 0;
                    });
                }
            });
        }
    });
}

// Añadir clase para animaciones progresivas basadas en scroll
document.addEventListener('scroll', function() {
    const elements = document.querySelectorAll('.post, .mini-post, .blurb, .posts article');
    
    elements.forEach(element => {
        const position = element.getBoundingClientRect();
        
        // Si el elemento está en el viewport
        if(position.top < window.innerHeight && position.bottom >= 0) {
            element.classList.add('visible');
        }
    });
});

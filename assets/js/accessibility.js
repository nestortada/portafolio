// Accessibility and Translation Logic

document.addEventListener('DOMContentLoaded', () => {
    // Inject Accessibility Widget HTML
    const widgetHTML = `
    <div id="accessibility-widget" class="accessibility-widget">
        <button id="accessibility-toggle" class="accessibility-toggle">
            <i class="fas fa-universal-access"></i>
        </button>
        <div id="accessibility-menu" class="accessibility-menu">
            <div class="acc-item">
                <span>Language / Idioma</span>
                <div class="acc-buttons">
                    <button onclick="setLanguage('es')" class="lang-btn" id="btn-es">ES</button>
                    <button onclick="setLanguage('en')" class="lang-btn" id="btn-en">EN</button>
                </div>
            </div>
            <div class="acc-item">
                <span>Font Size / Tamaño</span>
                <button id="toggle-fontsize" class="acc-action-btn">A+</button>
            </div>
            <div class="acc-item">
                <span>Motion / Movimiento</span>
                <button id="toggle-motion" class="acc-action-btn"><i class="fas fa-pause"></i></button>
            </div>
        </div>
    </div>
    <style>
        .accessibility-widget {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 10000;
            font-family: "Source Sans Pro", Helvetica, sans-serif;
        }
        .accessibility-toggle {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: #2ebaae;
            color: white;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            font-size: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s;
        }
        .accessibility-toggle:hover {
            transform: scale(1.1);
        }
        .accessibility-menu {
            display: none;
            position: absolute;
            bottom: 60px;
            right: 0;
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.2);
            width: 200px;
            flex-direction: column;
            gap: 10px;
        }
        .accessibility-menu.active {
            display: flex;
        }
        .acc-item {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }
        .acc-item span {
            font-size: 12px;
            font-weight: bold;
            color: #333;
        }
        .acc-buttons {
            display: flex;
            gap: 5px;
        }
        .lang-btn, .acc-action-btn {
            background: #f4f4f4;
            border: 1px solid #ddd;
            padding: 5px 10px;
            cursor: pointer;
            border-radius: 4px;
            flex: 1;
            font-size: 14px;
        }
        .lang-btn.active {
            background: #2ebaae;
            color: white;
            border-color: #2ebaae;
        }
        .acc-action-btn:hover {
            background: #e0e0e0;
        }
        
        /* Large Font Support */
        body.fontsize-large {
            font-size: 120%;
        }
        body.fontsize-large h1 { font-size: 2.5em; }
        body.fontsize-large h2 { font-size: 2em; }
        body.fontsize-large p { font-size: 1.2em; }

        /* Dark Mode overrides for menu */
        body.is-dark-mode .accessibility-menu {
            background: #222;
            color: #fff;
        }
        body.is-dark-mode .acc-item span {
            color: #ddd;
        }
        body.is-dark-mode .lang-btn, body.is-dark-mode .acc-action-btn {
            background: #333;
            border-color: #444;
            color: #fff;
        }
        body.is-dark-mode .lang-btn.active {
            background: #2ebaae;
            color: #fff;
        }
    </style>
    `;

    document.body.insertAdjacentHTML('beforeend', widgetHTML);

    // Event Listeners
    const toggleBtn = document.getElementById('accessibility-toggle');
    const menu = document.getElementById('accessibility-menu');
    const fontSizeBtn = document.getElementById('toggle-fontsize');
    const motionBtn = document.getElementById('toggle-motion');

    toggleBtn.addEventListener('click', () => {
        menu.classList.toggle('active');
    });

    // Font Size
    fontSizeBtn.addEventListener('click', () => {
        document.body.classList.toggle('fontsize-large');
        const isLarge = document.body.classList.contains('fontsize-large');
        fontSizeBtn.classList.toggle('active', isLarge);
        localStorage.setItem('pref-fontsize', isLarge ? 'large' : 'normal');
    });

    // Motion
    motionBtn.addEventListener('click', () => {
        const isPaused = window.toggle3DAnimation ? window.toggle3DAnimation() : false;
        motionBtn.innerHTML = isPaused ? '<i class="fas fa-play"></i>' : '<i class="fas fa-pause"></i>';
        motionBtn.classList.toggle('active', isPaused);
        localStorage.setItem('pref-motion', isPaused ? 'reduced' : 'normal');
    });

    // Initialize Preferences
    if (localStorage.getItem('pref-fontsize') === 'large') {
        document.body.classList.add('fontsize-large');
        fontSizeBtn.classList.add('active');
    }

    // Check system preference for simplified motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (localStorage.getItem('pref-motion') === 'reduced' || prefersReducedMotion) {
        // We need to wait for background-3d to load, so we use a small timeout or just set the flag
        window.disable3DAnimation = true;
        motionBtn.innerHTML = '<i class="fas fa-play"></i>';
        motionBtn.classList.add('active');
    }

    // Initialize Language
    const savedLang = localStorage.getItem('pref-lang') || 'es';
    setLanguage(savedLang);
});

// Global function to set language
window.setLanguage = function (lang) {
    if (!translations[lang]) return;

    // Update active button state
    document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.remove('active'));
    const activeBtn = document.getElementById(`btn-${lang}`);
    if (activeBtn) activeBtn.classList.add('active');

    // Update Text Content
    const elements = document.querySelectorAll('[data-i18n]');
    elements.forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[lang][key]) {
            // Check if element has HTML content or just text
            if (el.innerHTML.includes('<') && !el.innerHTML.includes('<strong>')) {
                // Be careful with replacing HTML structures
                // Ideally valid keys contain HTML safe strings or we use innerHTML
                el.innerHTML = translations[lang][key];
            } else {
                el.innerHTML = translations[lang][key];
            }
        }
    });

    // Special handling for placeholders
    const inputs = document.querySelectorAll('input[name="query"]');
    inputs.forEach(input => {
        if (translations[lang]['search.placeholder']) {
            input.placeholder = translations[lang]['search.placeholder'];
        }
    });

    localStorage.setItem('pref-lang', lang);
    document.documentElement.lang = lang;
};

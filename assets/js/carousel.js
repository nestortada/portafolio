document.addEventListener('DOMContentLoaded', () => {
    const carouselContainer = document.querySelector('#carouselExampleCaptions .carousel-inner');
    const projectListContainer = document.getElementById('project-list');

    // Determine category from body or URL
    let category = '';
    const path = window.location.pathname;
    if (path.includes('Industrial.html')) category = 'industrial';
    else if (path.includes('Informatica.html')) category = 'informatica';
    else if (path.includes('Otros.html')) category = 'otros';

    if (!category || !permissions[category]) return;

    // Filter projects
    const projects = projectsData.filter(p => p.category === category);

    // Generate Carousel Items
    if (carouselContainer) {
        carouselContainer.innerHTML = '';
        projects.forEach((project, index) => {
            const isActive = index === 0 ? 'active' : '';
            const item = document.createElement('div');
            item.className = `carousel-item ${isActive}`;

            item.innerHTML = `
                <a href="${project.link}">
                    <img src="${project.image}" class="d-block w-100" alt="${project.title}">
                </a>`;
            if (project.title) {
                const itemCaption = document.createElement('div');
                itemCaption.className = 'carousel-caption d-none d-md-block';
                // Inline color is strictly used only if defined, but we remove !important to allow Dark Mode override
                itemCaption.innerHTML = `<h5><a href="${project.link}" target="_blank" style="color: ${project.color || 'white'};">${project.title}</a></h5>`;
                item.appendChild(itemCaption);
            }
            carouselContainer.appendChild(item);
        });
    }

    // Generate Project List
    if (projectListContainer) {
        const listHeader = document.createElement('h3');
        listHeader.textContent = "Lista de Proyectos";
        // Check if there's a translation key for this header, otherwise default
        // listHeader.setAttribute('data-i18n', 'projects.list.title'); 

        const listElement = document.createElement('ul');
        listElement.className = "alt"; // Using existing class if available or just simple list

        projects.forEach(project => {
            const listItem = document.createElement('li');
            listItem.innerHTML = `<a href="${project.link}">${project.title}</a>`;
            listElement.appendChild(listItem);
        });

        projectListContainer.appendChild(listHeader);
        projectListContainer.appendChild(listElement);
    }
});

// Helper validation (optional, can be removed if not needed)
const permissions = {
    'industrial': true,
    'informatica': true,
    'otros': true
};

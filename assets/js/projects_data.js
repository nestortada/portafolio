const projectsData = [
    // Industrial Projects
    {
        category: "industrial",
        title: "Introducción a la Programación",
        image: "images/Intro_progra.jpg",
        link: "https://github.com/nestortada/Introduccion-a-la-programacion",
        color: "white"
    },
    {
        category: "industrial",
        title: "Probabilidad y Estadística 1",
        image: "images/Proba 1.jpg",
        link: "https://github.com/nestortada/Probabilidad-y-estadistica/tree/main/Probabilidad%20y%20estadistica%201",
        color: "white"
    },
    {
        category: "industrial",
        title: "Programación Avanzada",
        image: "images/Progra_Avanzada.jpg",
        link: "https://github.com/nestortada/Programaci-n-Avanzada",
        color: "white"
    },
    {
        category: "industrial",
        title: "Ingeniería de Metodos",
        image: "images/Inge_Metodos.jpg",
        link: "https://github.com/nestortada/Ingenieria_metodos",
        color: "white"
    },
    {
        category: "industrial",
        title: "Ingeniería Económica",
        image: "images/Inge_Economica.jpg",
        link: "https://github.com/nestortada/Ingenieria_economica",
        color: "white"
    },
    {
        category: "industrial",
        title: "Probabilidad y Estadística 2",
        image: "images/Proba 2.jpg",
        link: "https://github.com/nestortada/Probabilidad-y-estadistica/tree/main/Probabilidad%20y%20estadistica%202%20R",
        color: "black"
    },
    {
        category: "industrial",
        title: "Análisis de Diseño y Trabajo",
        image: "images/Tiempo.jpg",
        link: "https://github.com/nestortada/Analisis_Trabajo",
        color: "white"
    },
    {
        category: "industrial",
        title: "Analítica de Datos",
        image: "images/Analitica_Datos.jpg",
        link: "https://github.com/nestortada/Analitica-de-datos",
        color: "white"
    },
    {
        category: "industrial",
        title: "Contabilidad",
        image: "images/conta.jpg",
        link: "https://github.com/nestortada/Contabilidad",
        color: "white"
    },
    {
        category: "industrial",
        title: "Control Estadístico de la Calidad",
        image: "images/Calidad.jpg",
        link: "https://github.com/nestortada/Control_Estadistico_calidad",
        color: "white"
    },
    {
        category: "industrial",
        title: "Proceso Estocástico",
        image: "images/Estocasticos.jpg",
        link: "https://github.com/nestortada/Procesos_estocasticos",
        color: "white"
    },
    {
        category: "industrial",
        title: "Optimización y Analítica",
        image: "images/Optimizacion.jpg",
        link: "https://github.com/nestortada/Optimizacion_analitica",
        color: "gray"
    },
    {
        category: "industrial",
        title: "CAD",
        image: "images/CAD.jpg",
        link: "https://github.com/nestortada/CAD",
        color: "black"
    },
    {
        category: "industrial",
        title: "Simulación",
        image: "images/Sumulacion.jpeg",
        link: "https://github.com/nestortada/simulacion",
        color: "white"
    },

    // Informatica Projects
    {
        category: "informatica",
        title: "Introducción a la Programación",
        image: "images/Intro_progra.jpg",
        link: "https://github.com/nestortada/Introduccion-a-la-programacion",
        color: "white"
    },
    {
        category: "informatica",
        title: "Probabilidad y Estadística 1",
        image: "images/Proba 1.jpg",
        link: "https://github.com/nestortada/Probabilidad-y-estadistica/tree/main/Probabilidad%20y%20estadistica%201",
        color: "white"
    },
    {
        category: "informatica",
        title: "Programación Orientada a Objetos",
        image: "images/Objetos.jpg",
        link: "https://github.com/nestortada/programaci-n_orientada_objetos",
        color: "white"
    },
    {
        category: "informatica",
        title: "Probabilidad y Estadística 2",
        image: "images/Proba 2.jpg",
        link: "https://github.com/nestortada/Probabilidad-y-estadistica/tree/main/Probabilidad%20y%20estadistica%202%20R",
        color: "black"
    },
    {
        category: "informatica",
        title: "Analítica de Datos",
        image: "images/Analitica_Datos.jpg",
        link: "https://github.com/nestortada/Analitica-de-datos",
        color: "white"
    },
    {
        category: "informatica",
        title: "Machine Learning",
        image: "images/MachineLearning.jpeg",
        link: "https://github.com/nestortada/MACHINE-LEARNING-Clase",
        color: "white"
    },
    {
        category: "informatica",
        title: "Desarrollo Web",
        image: "images/DesarrolloWeb.png",
        link: "https://github.com/nestortada/DesarrolloWeb",
        color: "white"
    },
    {
        category: "informatica",
        title: "ETL",
        image: "images/ETL.jpeg",
        link: "https://github.com/nestortada/etl",
        color: "white"
    },

    // Otros Projects
    {
        category: "otros",
        title: "Portafolio",
        image: "images/Portafolio.jpg",
        link: "https://github.com/nestortada/portafolio",
        color: "black"
    },
    {
        category: "industrial",
        title: "Planeación, programación y control de las Operaciones",
        image: "images/Planeación, programación y control de las Operacionesjpeg.jpeg",
        link: "https://github.com/nestortada/Planeaciono",
        color: "white"
    },
    {
        category: "industrial",
        title: "Vizualización de Herramientas",
        image: "images/Vizualización de Herramientas.jpeg",
        link: "https://github.com/nestortada/Visualizacion-de-Herramientas-con-powerBI",
        color: "white"
    },
    {
        category: "industrial",
        title: "Gestión de Proyectos",
        image: "images/Gestión de Proyectos.jpg",
        link: "https://github.com/nestortada/Gestion-de-proyectos",
        color: "white"
    },
    {
        category: "industrial",
        title: "Gestión de la Calidad",
        image: "images/Gestión de la Calidad.png",
        link: "https://github.com/nestortada/Gesti-n-de-la-Calidad",
        color: "white"
    },
    {
        category: "industrial",
        title: "Fundamentos de Logística",
        image: "images/Fundamentos de Losgitica.jpg",
        link: "https://github.com/nestortada/Fundamentos-de-Losgitica",
        color: "white"
    }
];

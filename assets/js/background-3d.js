// 3D Background Animation using Three.js

document.addEventListener('DOMContentLoaded', () => {
    // Check if Three.js is loaded
    if (typeof THREE === 'undefined') {
        console.error('Three.js is not loaded.');
        return;
    }

    // Identify the container - creating a fixed canvas for background
    const container = document.createElement('div');
    container.id = 'canvas-container';
    container.style.position = 'fixed';
    container.style.top = '0';
    container.style.left = '0';
    container.style.width = '100%';
    container.style.height = '100%';
    container.style.zIndex = '-1';
    container.style.overflow = 'hidden';
    container.style.pointerEvents = 'none'; // Allow clicking through
    document.body.prepend(container);

    // Scene setup
    const scene = new THREE.Scene();
    // Use a fog to make distant particles fade out
    scene.fog = new THREE.FogExp2(0x000000, 0.002);

    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 100;

    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight);
    // Transparent background
    renderer.setClearColor(0x000000, 0);
    container.appendChild(renderer.domElement);

    // Particles (Nodes)
    const particleCount = 150;
    const particles = new THREE.BufferGeometry();
    const particlePositions = new Float32Array(particleCount * 3);
    const particleVelocities = [];

    const range = 200;

    for (let i = 0; i < particleCount; i++) {
        const x = (Math.random() - 0.5) * range;
        const y = (Math.random() - 0.5) * range;
        const z = (Math.random() - 0.5) * range;

        particlePositions[i * 3] = x;
        particlePositions[i * 3 + 1] = y;
        particlePositions[i * 3 + 2] = z;

        particleVelocities.push({
            x: (Math.random() - 0.5) * 0.2, // Fluid slow movement
            y: (Math.random() - 0.5) * 0.2,
            z: (Math.random() - 0.5) * 0.2
        });
    }

    particles.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));

    // Material for dots
    const particleMaterial = new THREE.PointsMaterial({
        color: 0x00aaff, // Cyan/Blueish for tech feel
        size: 1.5,
        transparent: true,
        opacity: 0.8
    });

    const particleSystem = new THREE.Points(particles, particleMaterial);
    scene.add(particleSystem);

    // Lines setup
    const lineMaterial = new THREE.LineBasicMaterial({
        color: 0x00aaff,
        transparent: true,
        opacity: 0.3
    });

    const linesGeometry = new THREE.BufferGeometry();
    const lines = new THREE.LineSegments(linesGeometry, lineMaterial);
    scene.add(lines);

    // Mouse Interaction
    const mouse = new THREE.Vector2();
    let mouseX = 0;
    let mouseY = 0;

    // Slight parallax effect based on mouse
    document.addEventListener('mousemove', (event) => {
        mouseX = event.clientX - window.innerWidth / 2;
        mouseY = event.clientY - window.innerHeight / 2;
    });

    // Animation Loop
    function animate() {
        requestAnimationFrame(animate);

        // Update particle positions
        const positions = particleSystem.geometry.attributes.position.array;

        for (let i = 0; i < particleCount; i++) {
            // Update position
            positions[i * 3] += particleVelocities[i].x;
            positions[i * 3 + 1] += particleVelocities[i].y;
            positions[i * 3 + 2] += particleVelocities[i].z;

            // Boundary check - bounce back softly
            if (Math.abs(positions[i * 3]) > range / 2) particleVelocities[i].x *= -1;
            if (Math.abs(positions[i * 3 + 1]) > range / 2) particleVelocities[i].y *= -1;
            if (Math.abs(positions[i * 3 + 2]) > range / 2) particleVelocities[i].z *= -1;
        }

        particleSystem.geometry.attributes.position.needsUpdate = true;

        // Draw connections (Plexus effect)
        updateLines(positions);

        // Camera movement (Parallax)
        camera.position.x += (mouseX * 0.05 - camera.position.x) * 0.05;
        camera.position.y += (-mouseY * 0.05 - camera.position.y) * 0.05;
        camera.lookAt(scene.position);

        renderer.render(scene, camera);
    }

    function updateLines(positions) {
        const connectDistance = 35; // Connection threshold
        const linePositions = [];

        // This is O(n^2), but for 100-200 particles it's fine for desktop
        for (let i = 0; i < particleCount; i++) {
            for (let j = i + 1; j < particleCount; j++) {
                const dx = positions[i * 3] - positions[j * 3];
                const dy = positions[i * 3 + 1] - positions[j * 3 + 1];
                const dz = positions[i * 3 + 2] - positions[j * 3 + 2];
                const dist = Math.sqrt(dx * dx + dy * dy + dz * dz);

                if (dist < connectDistance) {
                    // Add both points to the line segments
                    linePositions.push(
                        positions[i * 3], positions[i * 3 + 1], positions[i * 3 + 2],
                        positions[j * 3], positions[j * 3 + 1], positions[j * 3 + 2]
                    );
                }
            }
        }

        linesGeometry.setAttribute('position', new THREE.Float32BufferAttribute(linePositions, 3));
    }

    // Handle Resize
    window.addEventListener('resize', () => {
        camera.aspect = window.innerWidth / window.innerHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(window.innerWidth, window.innerHeight);
    });

    animate();
});

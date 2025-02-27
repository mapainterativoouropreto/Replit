document.addEventListener('DOMContentLoaded', function() {
    console.log('Initializing map zoom functionality...');

    // Initialize zoom functionality for all maps
    const maps = document.querySelectorAll('.mapa-container');
    console.log(`Found ${maps.length} zoomable maps`);

    maps.forEach((container, index) => {
        const map = container.querySelector('img');
        console.log(`Initializing zoom for map ${index + 1}`);

        try {
            // Prevent scroll default behavior when hovering over map
            container.addEventListener('wheel', function(e) {
                e.preventDefault();
            }, { passive: false });

            const wheelZoom = WZoom.create(map, {
                maxScale: 10,
                speed: 0.1,
                zoomOnClick: true,
                zoomWithWheel: true,
                dragScrollableOptions: {
                    onGrab: () => {
                        map.style.cursor = 'grabbing';
                        console.log(`Map ${index + 1}: Grab started`);
                    },
                    onDrop: () => {
                        map.style.cursor = 'grab';
                        console.log(`Map ${index + 1}: Grab ended`);
                    }
                }
            });

            // Reset zoom on double click
            container.addEventListener('dblclick', (e) => {
                e.preventDefault();
                console.log(`Map ${index + 1}: Resetting zoom`);
                wheelZoom.reset();
            });

            // Set initial cursor style
            map.style.cursor = 'grab';

            console.log(`Map ${index + 1}: Zoom initialization complete`);
        } catch (error) {
            console.error(`Error initializing zoom for map ${index + 1}:`, error);
        }
    });
});
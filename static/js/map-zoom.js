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

            const wheelZoom = WZoom.create(container, {
                type: 'html',
                width: container.clientWidth,
                height: container.clientHeight,
                minScale: 0.5,
                maxScale: 10,
                speed: 1,
                zoomOnClick: true,
                // Enable zoom with mouse wheel
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
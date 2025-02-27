document.addEventListener('DOMContentLoaded', function() {
    console.log('Initializing map zoom functionality...');

    // Initialize zoom functionality for all maps
    const maps = document.querySelectorAll('.zoomable-map');
    console.log(`Found ${maps.length} zoomable maps`);

    maps.forEach((map, index) => {
        console.log(`Initializing zoom for map ${index + 1}`);
        try {
            const wheelZoom = WZoom.create(map, {
                type: 'html',
                width: map.clientWidth,
                height: map.clientHeight,
                minScale: 1,
                maxScale: 4,
                speed: 0.8,
                zoomOnClick: false,
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
            map.addEventListener('dblclick', () => {
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
$( document ).ready(function() {
    // Scroll Position

    $(window).scroll(function(){
        let scrollPos = $(document).scrollTop();
        let selectedElement = $('.navbar');
        if (scrollPos > 100) {
            selectedElement.css({
                'position': 'fixed',
                'width': '100%',
                'transition': 'all 1s ease-in-out',
                'z-index': '1000000',
            });
        } else {
            selectedElement.css({
                'position': 'relative',
                'transition': 'all 1s ease-in-out'
            });
        }
    });

    // Initialize AOS
    AOS.init();
    console.log( "ready!" );
});
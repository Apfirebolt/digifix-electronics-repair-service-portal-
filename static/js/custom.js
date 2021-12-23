$(document).ready(function() {
    $('#close-menu').click(() => {
        $('#mobile-nav').slideToggle();
    })
    // Scroll Position
    $(window).scroll(function(){
        let scrollPos = $(document).scrollTop();
        let selectedElement = $('.nav-container');
        if (scrollPos > 100) {
            selectedElement.addClass('sticky z-50 top-0 bg-green-100 transition ease-out duration-1000 text-white');
        } else {
            selectedElement.removeClass('sticky z-50 top-0 bg-green-100 transition ease-out duration-1000 text-white')
        }
    });
    // Initialize AOS
    AOS.init();
});
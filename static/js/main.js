window.addEventListener('scroll', function() {
    document.getElementById('header-nav').classList.toggle('headernav-scroll', window.scrollY > 135);
});

$(document).ready(function(){
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('#top').fadeIn();
        } else {
            $('#top').fadeOut();
        }
    });

    $('#top').click(function () {
        $('html, body').animate({scrollTop: 0}, 500);
        return false;
    });

    $(".owl-carousel-full").owlCarousel($('.owl-carousel').owlCarousel({
        margin:20,
        responsive:{
            0:{
                items:1
            },
            500:{
                items:2
            },
            700:{
                items:3
            },
            1000:{
                items:4
            },
            1300:{
                items:5
            },
            1600:{
                items:6
            },
        }
    }));
});

(() => {
    'use strict'

    const forms = document.querySelectorAll('.needs-validation')

    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

            form.classList.add('was-validated')
        }, false)
    })
})()


const canvas_small = document.getElementById('canvas-small');
canvas_small.width = 960;
canvas_small.height = 800;

const context_small = canvas_small.getContext('2d');

context_small.fillStyle = 'white';
context_small.fillRect(10, 10, 100, 50);


// const canvas_medium = document.getElementById('canvas-medium');
// canvas_medium.width = 900;
// canvas_medium.height = 850;
//
// const context_medium = canvas_medium.getContext('2d');
//
// context_medium.fillStyle = 'white';
// context_medium.fillRect(10, 10, 100, 50);
//
//
// const canvas_large = document.getElementById('canvas-large');
// canvas_large.width = 780;
// canvas_large.height = 660;
//
// const context_large = canvas_large.getContext('2d');
//
// context_large.fillStyle = 'white';
// context_large.fillRect(10, 10, 100, 50);

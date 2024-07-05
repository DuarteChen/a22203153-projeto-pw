document.addEventListener("DOMContentLoaded", function() {
    init();
    showSlides(slideIndex);
});

function init() {
    const btn = document.querySelector("#menu_toggle");

    document.addEventListener("click", documentEvents);
}

function documentEvents(event) {
    console.log(event);

    const nav = document.querySelector("#menu_navigation");
    if (event.target.id === "menu_toggle") {
        nav.classList.toggle("is_active");
    } else {
        nav.classList.remove("is_active");
    }
}

let slideIndex = 1;

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}

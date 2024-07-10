document.addEventListener("DOMContentLoaded", function() {
    init();
    showSlides(slideIndex);
});

function init() {
    const btn = document.querySelector("#menu_toggle");
    const btnThemePurple = document.querySelector("#purpleButton");

    btn.addEventListener("click", function() {
        document.querySelector("#menu_navigation").classList.toggle("is_active");
    });

    btnThemePurple.addEventListener("click", function() {
        document.body.classList.toggle("purple-theme");


        const isPurpleTheme = document.body.classList.contains("purple-theme");
        localStorage.setItem("purpleTheme", isPurpleTheme ? "enabled" : "disabled");
    });


    const storedTheme = localStorage.getItem("purpleTheme");
    if (storedTheme === "enabled") {
        document.body.classList.add("purple-theme");
    }

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


    if (!event.target.closest("#menu_navigation") && !event.target.closest("#menu_toggle")) {
        nav.classList.remove("is_active");
    }
}

let slideIndex = 1;

function plusSlides(n) {
    showSlides(slideIndex += n);
}

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

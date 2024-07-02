document.addEventListener("DOMContentLoaded", init);

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



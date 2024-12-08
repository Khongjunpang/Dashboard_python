let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
/*let searchBtn = document.querySelector(".bx-search");*/

closeBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    menuBtnChange();
})

/*searchBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    menuBtnChange();
})*/

function menuBtnChange() {
    if (sidebar.classList.contains("open")) {
        closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
        sidebar.style.width = '250px';
        document.getElementById("mySidepanel").style.width = "250px";
    } else {
        closeBtn.classList.replace("bx-menu-alt-right", "bx-menu");
        sidebar.style.width = '78px';
        document.getElementById("mySidepanel").style.width = "0";
    }
}

menuBtnChange();


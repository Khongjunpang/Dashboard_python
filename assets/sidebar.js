document.addEventListener("DOMContentLoaded", function() {
    let sidebar = document.querySelector(".sidebar");
    let closeBtn = document.querySelector("#btn");

    if (closeBtn) {
        closeBtn.addEventListener("click", () => {
            if (sidebar) {
                sidebar.classList.toggle("open");
                menuBtnChange();
            } else {
                console.error("Sidebar element not found.");
            }
        });

        function menuBtnChange() {
            if (sidebar && closeBtn) {
                if (sidebar.classList.contains("open")) {
                    closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
                    sidebar.style.width = '250px';
                } else {
                    closeBtn.classList.replace("bx-menu-alt-right", "bx-menu");
                    sidebar.style.width = '78px';
                }
            }
        }

        menuBtnChange();
    } else {
        console.error("Element with ID 'btn' not found.");
    }
});

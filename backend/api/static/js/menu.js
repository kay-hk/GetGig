document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.getElementById("menu-icon");
    const navbar = document.querySelector(".navbar");
    const navLinks = document.querySelectorAll(".navbar a");

    if (!menuIcon || !navbar) {
        console.error("❌ Error: Menu icon or navbar not found!");
        return;
    }

    // Toggle the navbar visibility
    menuIcon.addEventListener("click", function () {
        navbar.classList.toggle("open");

        if (navbar.classList.contains("open")) {
            navbar.style.display = "flex"; // Ensure navbar is visible
            setTimeout(() => {
                navbar.style.opacity = "1"; // Fade in
            }, 50);
        } else {
            navbar.style.opacity = "0"; // Fade out
            setTimeout(() => {
                navbar.style.display = "none"; // Hide after fade-out
            }, 500); // Match the CSS transition duration
        }
    });

    // Optional: Close the navbar when a link is clicked
    navLinks.forEach(link => {
        link.addEventListener("click", () => {
            navbar.classList.remove("open");
            navbar.style.opacity = "0";
            setTimeout(() => {
                navbar.style.display = "none";
            }, 500);
        });
    });
});
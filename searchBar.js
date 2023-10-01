document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("searchInput");
    const searchButton = document.getElementById("searchButton");

    searchButton.addEventListener("click", scrollToElement);
    searchInput.addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            scrollToElement();
        }
    });

    function scrollToElement() {
        const idToScrollTo = searchInput.value;
        const elementToScrollTo = document.getElementById(idToScrollTo);

        if (elementToScrollTo) {
            elementToScrollTo.scrollIntoView({ behavior: "smooth" });
        } else {
            alert("Element with ID not found!");
        }
    }
});

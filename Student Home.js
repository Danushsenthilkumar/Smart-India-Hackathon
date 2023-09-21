document.addEventListener("DOMContentLoaded", function () {
    // Get references to all feature sections
    const featureSections = document.querySelectorAll(".feature");

    // Loop through each feature section
    featureSections.forEach(function (feature, index) {
        // Add a click event listener to each feature
        feature.addEventListener("click", function () {
            // Toggle the class to hide or show feature content
            feature.classList.toggle("expanded");

            // Loop through all feature sections again to collapse others
            featureSections.forEach(function (otherFeature, otherIndex) {
                if (index !== otherIndex) {
                    otherFeature.classList.remove("expanded");
                }
            });
        });
    });
});

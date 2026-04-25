document.addEventListener('DOMContentLoaded', function() {

    const electricityButton = document.getElementById("electricity-button");

    electricityButton.addEventListener("click", function() {

        window.location.href = "electricity"
        
    });

});

document.addEventListener('DOMContentLoaded', function() {

    const mechanicsButton = document.getElementById("mechanics-button");

    mechanicsButton.addEventListener("click", function() {

        window.location.href = "mechanics"
        
    });

});

document.addEventListener('DOMContentLoaded', function() {

    const thermodynamicsButton = document.getElementById("thermodynamics-button");

    thermodynamicsButton.addEventListener("click", function() {

        window.location.href = "thermodynamics"
        
    });

});
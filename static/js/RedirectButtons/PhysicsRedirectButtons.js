document.addEventListener('DOMContentLoaded', function() {

    const electricityButton = document.getElementById("electricity-button");

    electricityButton.addEventListener("click", function() {

        window.location.href = "electricity"
        
    });

});

document.addEventListener('DOMContentLoaded', function() {

    const mechanicButton = document.getElementById("mechanic-button");

    mechanicButton.addEventListener("click", function() {

        window.location.href = "mechanic"
        
    });

});

document.addEventListener('DOMContentLoaded', function() {

    const thermodynamicButton = document.getElementById("thermodynamic-button");

    thermodynamicButton.addEventListener("click", function() {

        window.location.href = "thermodynamic"
        
    });

});
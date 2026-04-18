import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const densityInput = document.getElementById("archimedes-force-density");
    const gravityAccelerationInput = document.getElementById("archimedes-force-gravity-acceleration");
    const volumeInput = document.getElementById("archimedes-force-volume");
    const massInput = document.getElementById("archimedes-force-mass");
    const calculateButton = document.getElementById("calculate-archimedes-force-button");
    const resultOutput = document.getElementById("archimedes-force-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_archimedes_force",
                data: {
                    density: densityInput.value || null,
                    gravity_acceleration: gravityAccelerationInput.value || null,
                    volume: volumeInput.value || null,
                    mass: massInput.value || null,
                }
            })
        })
        .then(response => response.json())
        .then(data => {
            const answer = data.result;
            const answerIsNotNull = answer !== null;

            if (answerIsNotNull) {
                resultOutput.innerText = `${answerPhrase}${answer}`;
            } else {
                resultOutput.innerText = errorPhrase;
            }
        });
    });
});
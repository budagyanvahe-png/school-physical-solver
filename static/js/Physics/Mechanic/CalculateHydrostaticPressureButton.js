import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const densityInput = document.getElementById("hydrostatic-pressure-density");
    const gravityAccelerationInput = document.getElementById("hydrostatic-pressure-gravity-acceleration");
    const heightInput = document.getElementById("hydrostatic-pressure-height");
    const calculateButton = document.getElementById("calculate-hydrostatic-pressure-button");
    const resultOutput = document.getElementById("hydrostatic-pressure-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_hydrostatic_pressure",
                data: {
                    density: densityInput.value || null,
                    gravity_acceleration: gravityAccelerationInput.value || null,
                    height: heightInput.value || null,
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
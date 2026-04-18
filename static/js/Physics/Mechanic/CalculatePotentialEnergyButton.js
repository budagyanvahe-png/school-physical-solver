import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const massInput = document.getElementById("potential-energy-mass");
    const accelerationInput = document.getElementById("potential-energy-acceleration");
    const heightInput = document.getElementById("potential-energy-height");
    const hardnessInput = document.getElementById("potential-energy-hardness");
    const startLengthInput = document.getElementById("potential-energy-start-length");
    const endLengthInput = document.getElementById("potential-energy-end-length");
    const deltaLengthInput = document.getElementById("potential-energy-delta-length");
    const calculateButton = document.getElementById("calculate-potential-energy-button");
    const resultOutput = document.getElementById("potential-energy-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_potential_energy",
                data: {
                    mass: massInput.value || null,
                    acceleration: accelerationInput.value || null,
                    height: heightInput.value || null,
                    hardness: hardnessInput.value || null,
                    start_length: startLengthInput.value || null,
                    end_length: endLengthInput.value || null,
                    delta_length: deltaLengthInput.value || null,
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
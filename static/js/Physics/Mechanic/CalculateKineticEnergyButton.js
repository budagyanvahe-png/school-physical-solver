import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const massInput = document.getElementById("kinetic-energy-mass");
    const velocityInput = document.getElementById("kinetic-energy-velocity");
    const impulseInput = document.getElementById("kinetic-energy-impulse");
    const calculateButton = document.getElementById("calculate-kinetic-energy-button");
    const resultOutput = document.getElementById("kinetic-energy-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_kinetic_energy",
                data: {
                    mass: massInput.value || null,
                    velocity: velocityInput.value || null,
                    impulse: impulseInput.value || null,
                }
            })
        })
        .then(responce => responce.json())
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
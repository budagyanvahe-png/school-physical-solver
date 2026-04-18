import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const totalForceInput = document.getElementById("mechanical-work-total-force");
    const elapsedDistanceInput = document.getElementById("mechanical-work-elapsed-distance");
    const angleInput = document.getElementById("mechanical-work-angle");
    const startKineticEnergy = document.getElementById("mechanical-work-start-kinetic-energy");
    const endKineticEnergy = document.getElementById("mechanical-work-end-kinetic-energy");
    const calculateButton = document.getElementById("calculate-mechanical-work-button");
    const resultOutput = document.getElementById("mechanical-work-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_mechanical_work",
                data: {
                    total_force: totalForceInput.value || null,
                    elapsed_distance: elapsedDistanceInput.value || null,
                    angle: angleInput.value || null,
                    start_kinetic_energy: startKineticEnergy.value || null,
                    end_kinetic_energy: endKineticEnergy.value || null,
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
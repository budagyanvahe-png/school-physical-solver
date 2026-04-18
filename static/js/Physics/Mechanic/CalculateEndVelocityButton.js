import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const deltaVelocityInput = document.getElementById("end-velocity-delta-velocity");
    const startVelocityInput = document.getElementById("end-velocity-start-velocity");
    const accelerationInput = document.getElementById("end-velocity-acceleration");
    const elapsedDistanceInput = document.getElementById("end-velocity-elapsed-distance");
    const elapsedTimeInput = document.getElementById("end-velocity-elapsed-time");
    const averageVelocityInput = document.getElementById("end-velocity-average-velocity");
    const calculateButton = document.getElementById("calculate-end-velocity-button");
    const resultOutput = document.getElementById("end-velocity-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_end_velocity",
                data: {
                    delta_velocity: deltaVelocityInput.value || null,
                    start_velocity: startVelocityInput.value || null,
                    acceleration: accelerationInput.value || null,
                    elapsed_distance: elapsedDistanceInput.value || null,
                    elapsed_time: elapsedTimeInput.value || null,
                    average_velocity: averageVelocityInput.value || null,
                },
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
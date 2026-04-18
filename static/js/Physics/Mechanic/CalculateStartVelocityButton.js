import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const deltaVelocityInput = document.getElementById("start-velocity-delta-velocity");
    const endVelocityInput = document.getElementById("start-velocity-end-velocity");
    const accelerationInput = document.getElementById("start-velocity-acceleration");
    const elapsedTimeInput = document.getElementById("start-velocity-elapsed-time");
    const elapsedDistanceInput = document.getElementById("start-velocity-elapsed-distance");
    const averageVelocityInput = document.getElementById("start-velocity-average-velocity");
    const calculateButton = document.getElementById("calculate-start-velocity-button");
    const resultOutput = document.getElementById("start-velocity-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_start_velocity",
                data: {
                    delta_velocity: deltaVelocityInput.value || null,
                    end_velocity: endVelocityInput.value || null,
                    acceleration: accelerationInput.value || null,
                    elapsed_time: elapsedTimeInput.value || null,
                    elapsed_distance: elapsedDistanceInput.value || null,
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
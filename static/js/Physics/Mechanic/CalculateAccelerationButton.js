import { errorPhrase, answerPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const startVelocityInput = document.getElementById("acceleration-start-velocity");
    const endVelocityInput = document.getElementById("acceleration-end-velocity");
    const elapsedTimeInput = document.getElementById("acceleration-elapsed-time");
    const deltaVelocityInput = document.getElementById("acceleration-delta-velocity");
    const elapsedDistanceInput = document.getElementById("acceleration-elapsed-distance");
    const totalForceInput = document.getElementById("acceleration-total-force");
    const massInput = document.getElementById("acceleration-mass");
    const calculateButton = document.getElementById("calculate-acceleration-button");
    const resultOutput = document.getElementById("acceleration-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-Type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_acceleration",
                data: {
                    start_velocity: startVelocityInput.value || null,
                    end_velocity: endVelocityInput.value || null,
                    elapsed_time: elapsedTimeInput.value || null,
                    delta_velocity: deltaVelocityInput.value || null,
                    elapsed_distance: elapsedDistanceInput.value || null,
                    total_force: totalForceInput.value || null,
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
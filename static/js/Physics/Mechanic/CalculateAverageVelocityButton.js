import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const startVelocityInput = document.getElementById("average-velocity-start-velocity");
    const endVelocityInput = document.getElementById("average-velocity-end-velocity");
    const deltaVelocityInput = document.getElementById("average-velocity-delta-velocity");
    const accelerationInput = document.getElementById("average-velocity-acceleration");
    const elapsedTimeInput = document.getElementById("average-velocity-elapsed-time");
    const calculateButton = document.getElementById("calculate-average-velocity-button");
    const resultOutput = document.getElementById("average-velocity-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_average_velocity",
                data: {
                    start_velocity: startVelocityInput.value || null,
                    end_velocity: endVelocityInput.value || null,
                    delta_velocity: deltaVelocityInput.value || null,
                    acceleration: accelerationInput.value || null,
                    elapsed_time: elapsedTimeInput.value || null,
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
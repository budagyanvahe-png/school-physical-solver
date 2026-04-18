import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const slidingFrictionInput = document.getElementById("friction-force-sliding-friction");
    const supportReactionInput = document.getElementById("friction-force-support-reaction");
    const massInput = document.getElementById("friction-force-mass");
    const accelerationInput = document.getElementById("friction-force-acceleration");
    const angleInput = document.getElementById("friction-force-angle");
    const calculateButton = document.getElementById("calculate-friction-force-button");
    const resultOutput = document.getElementById("friction-force-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_friction_force",
                data: {
                    sliding_friction: slidingFrictionInput.value || null,
                    support_reaction: supportReactionInput.value || null,
                    mass: massInput.value || null,
                    acceleration: accelerationInput.value || null,
                    angle: angleInput.value || null,
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
import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const specificFusionHeatInput = document.getElementById("fusion-heat-specific-fusion-heat");
    const massInput = document.getElementById("fusion-heat-mass");
    const calculateButton = document.getElementById("calculate-fusion-heat-button");
    const resultOutput = document.getElementById("fusion-heat-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_fusion_heat",
                data: {
                    specific_fusion_heat: specificFusionHeatInput.value || null,
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
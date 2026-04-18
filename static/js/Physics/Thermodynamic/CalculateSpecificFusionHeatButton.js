import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const fusionHeatInput = document.getElementById("specific-fusion-heat-fusion-heat");
    const massInput = document.getElementById("specific-fusion-heat-mass");
    const calculateButton = document.getElementById("calculate-specific-fusion-heat-button");
    const resultOutput = document.getElementById("specific-fusion-heat-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_specific_fusion_heat",
                data: {
                    fusion_heat: fusionHeatInput.value || null,
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
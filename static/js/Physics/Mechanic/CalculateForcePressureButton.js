import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const forceInput = document.getElementById("force-pressure-force");
    const areaInput = document.getElementById("force-pressure-area");
    const calculateButton = document.getElementById("calculate-force-pressure-button");
    const resultOutput = document.getElementById("force-pressure-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_force_pressure",
                data: {
                    force: forceInput.value || null,
                    area: areaInput.value || null,
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
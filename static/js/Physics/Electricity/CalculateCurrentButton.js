import { errorPhrase, answerPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {

    const voltageInput = document.getElementById("current-voltage");
    const resistanceInput = document.getElementById("current-resistance");
    const dissipatedHeatInput = document.getElementById("current-dissipated-heat");
    const elapsedTimeInput = document.getElementById("current-elapsed-time");
    const electricalPowerInput = document.getElementById("current-electrical-power");
    const calculateButton = document.getElementById("calculate-current-button");
    const resultOutput = document.getElementById("current-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                formula_type: "get_current",
                data: {
                    voltage: voltageInput.value || null,
                    resistance: resistanceInput.value || null,
                    dissipated_heat: dissipatedHeatInput.value || null,
                    elapsed_time: elapsedTimeInput.value || null,
                    electrical_power: electricalPowerInput.value || null,
                }
            })
        })
        .then(response => response.json())
        .then(data => {
            const answer = data.result;
            const answerIsNotNull = answer !== null;

            if (answerIsNotNull){
                resultOutput.innerText = `${answerPhrase}${answer}`;
            } else {
                resultOutput.innerText = errorPhrase;
            }
        });
    });
});
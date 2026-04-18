import { errorPhrase, answerPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {

    const currentInput = document.getElementById("voltage-current");
    const resistanceInput = document.getElementById("voltage-resistance");
    const dissipatedHeatInput = document.getElementById("voltage-dissipated-heat");
    const elapsedTimeInput = document.getElementById("voltage-elapsed-time");
    const electricicalPowerInput = document.getElementById("voltage-electrical-power");
    const calculateButton = document.getElementById("calculate-voltage-button");
    const resultOutput = document.getElementById("voltage-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                formula_type: "get_voltage",
                data: {
                    current: currentInput.value || null,
                    resistance: resistanceInput.value || null,
                    dissipated_heat: dissipatedHeatInput.value || null,
                    elapsed_time: elapsedTimeInput.value || null,
                    electrical_power: electricicalPowerInput.value || null,
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
        })
    });
});
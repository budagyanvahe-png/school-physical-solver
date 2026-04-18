import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const voltageInput = document.getElementById("electrical-power-voltage");
    const currentInput = document.getElementById("electrical-power-current");
    const resistanceInput = document.getElementById("electrical-power-resistance");
    const dissipatedHeatInput = document.getElementById("electrical-power-dissipated-heat");
    const elapsedTimeInput = document.getElementById("electrical-power-elapsed-time");
    const calculateButton = document.getElementById("calculate-electrical-power-button");
    const resultOutput = document.getElementById("electrical-power-result");

    calculateButton.addEventListener("click", function(){
        fetch("/calculate", {
            headers: {"Content-Type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_electrical_power",
                data: {
                    voltage: voltageInput.value || null,
                    current: currentInput.value || null,
                    resistance: resistanceInput.value || null,
                    dissipated_heat: dissipatedHeatInput.value || null,
                    elapsed_time: elapsedTimeInput.value || null,
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
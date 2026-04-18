import { errorPhrase, answerPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    
    const currentInput = document.getElementById("joule-lenz-current");
    const resistanceInput = document.getElementById("joule-lenz-resistance");
    const elapsedTimeInput = document.getElementById("joule-lenz-elapsed-time");
    const voltageInput = document.getElementById("joule-lenz-voltage");
    const electricalPowerInput = document.getElementById("joule-lenz-electrical-power");
    const calculateButton = document.getElementById("calculate-dissipated-heat-button");
    const resultOutput = document.getElementById("dissipated-heat-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
                formula_type: "get_dissipated_heat",
                data: {
                    current: currentInput.value || null,
                    resistance: resistanceInput.value || null,
                    elapsed_time: elapsedTimeInput.value || null,
                    voltage: voltageInput.value || null,
                    electrical_power: electricalPowerInput.value || null,
                },
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
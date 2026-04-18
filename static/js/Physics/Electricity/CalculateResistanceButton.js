import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const voltageInput = document.getElementById("resistance-voltage");
    const currentInput = document.getElementById("resistance-current");
    const dissipdatedHeatInput = document.getElementById("resistance-dissipated-heat");
    const elapsedTimeInput = document.getElementById("resistance-elapsed-time");
    const electricalPowerInput = document.getElementById("resistance-electrical-power");
    const specificResistanceInput = document.getElementById("resistance-specific-resistance");
    const electricalConductorLength = document.getElementById("resistance-electrical-conductor-length");
    const conductorTransverseArea = document.getElementById("resistance-conductor-transverse-area");
    const calculateButton = document.getElementById("calculate-resistance-button");
    const resultOutput = document.getElementById("resistance-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-Type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_resistance",
                data: {
                    voltage: voltageInput.value || null,
                    current: currentInput.value || null,
                    dissipated_heat: dissipdatedHeatInput.value || null,
                    elapsed_time: elapsedTimeInput.value || null,
                    electrical_power: electricalPowerInput.value || null,
                    specific_resistance: specificResistanceInput.value || null,
                    electrical_conductor_length: electricalConductorLength.value || null,
                    conductor_transverse_area: conductorTransverseArea.value || null,
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
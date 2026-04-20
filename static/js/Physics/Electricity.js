import { errorPhrase, answerPhrase, calculateEndpoint } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {

    const voltageInput = document.getElementById("current-voltage");
    const resistanceInput = document.getElementById("current-resistance");
    const dissipatedHeatInput = document.getElementById("current-dissipated-heat");
    const elapsedTimeInput = document.getElementById("current-elapsed-time");
    const electricalPowerInput = document.getElementById("current-electrical-power");
    const calculateButton = document.getElementById("calculate-current-button");
    const resultOutput = document.getElementById("current-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
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

document.addEventListener("DOMContentLoaded", function() {
    
    const currentInput = document.getElementById("joule-lenz-current");
    const resistanceInput = document.getElementById("joule-lenz-resistance");
    const elapsedTimeInput = document.getElementById("joule-lenz-elapsed-time");
    const voltageInput = document.getElementById("joule-lenz-voltage");
    const electricalPowerInput = document.getElementById("joule-lenz-electrical-power");
    const calculateButton = document.getElementById("calculate-dissipated-heat-button");
    const resultOutput = document.getElementById("dissipated-heat-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
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

document.addEventListener("DOMContentLoaded", function() {
    const voltageInput = document.getElementById("electrical-power-voltage");
    const currentInput = document.getElementById("electrical-power-current");
    const resistanceInput = document.getElementById("electrical-power-resistance");
    const dissipatedHeatInput = document.getElementById("electrical-power-dissipated-heat");
    const elapsedTimeInput = document.getElementById("electrical-power-elapsed-time");
    const calculateButton = document.getElementById("calculate-electrical-power-button");
    const resultOutput = document.getElementById("electrical-power-result");

    calculateButton.addEventListener("click", function(){
        fetch(calculateEndpoint, {
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
        fetch(calculateEndpoint, {
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

document.addEventListener("DOMContentLoaded", function() {

    const currentInput = document.getElementById("voltage-current");
    const resistanceInput = document.getElementById("voltage-resistance");
    const dissipatedHeatInput = document.getElementById("voltage-dissipated-heat");
    const elapsedTimeInput = document.getElementById("voltage-elapsed-time");
    const electricicalPowerInput = document.getElementById("voltage-electrical-power");
    const calculateButton = document.getElementById("calculate-voltage-button");
    const resultOutput = document.getElementById("voltage-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
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
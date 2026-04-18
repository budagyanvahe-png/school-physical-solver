import { answerPhrase, errorPhrase } from "/static/js//config.js";

document.addEventListener("DOMContentLoaded", function() {
    const sensibleHeatInput = document.getElementById("specific-heat-sensible-heat");
    const massInput = document.getElementById("specific-heat-mass");
    const deltaTemperatureInput = document.getElementById("specific-heat-delta-temperature");
    const startTemperatureInput = document.getElementById("specific-heat-start-temperature");
    const endTemperatureInput = document.getElementById("specific-heat-end-temperature");
    const calculateButton = document.getElementById("calculate-specific-heat-button");
    const resultOutput = document.getElementById("specific-heat-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_specific_heat",
                data: {
                    sensible_heat: sensibleHeatInput.value || null,
                    mass: massInput.value || null,
                    delta_temperature: deltaTemperatureInput.value || null,
                    start_temperature: startTemperatureInput.value || null,
                    end_temperature: endTemperatureInput.value || null,
                }
            })
        })
        .then(responce => responce.json())
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
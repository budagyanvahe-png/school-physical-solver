import { answerPhrase, errorPhrase } from "/static/js//config.js";

document.addEventListener("DOMContentLoaded", function() {
    const specificHeatInput = document.getElementById("sensible-heat-specific-heat");
    const massInput = document.getElementById("sensible-heat-mass");
    const deltaTemperatureInput = document.getElementById("sensible-heat-delta-temperature");
    const startTemperatureInput = document.getElementById("sensible-heat-start-temperature");
    const endTemperatureInput = document.getElementById("sensible-heat-end-temperature");
    const calculateButton = document.getElementById("calculate-sensible-heat-button");
    const resultOutput = document.getElementById("sensible-heat-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_sensible_heat",
                data: {
                    specific_heat: specificHeatInput.value || null,
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
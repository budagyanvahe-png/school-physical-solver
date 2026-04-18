import { answerPhrase, errorPhrase } from "/static/js//config.js";

document.addEventListener("DOMContentLoaded", function() {
    const sensibleHeatInput = document.getElementById("delta-temperature-sensible-heat");
    const specificHeatInput = document.getElementById("delta-temperature-specific-heat");
    const massInput = document.getElementById("delta-temperature-mass");
    const startTemperatureInput = document.getElementById("delta-temperature-start-temperature");
    const endTemperatureInput = document.getElementById("delta-temperature-end-temperature");
    const calculateButton = document.getElementById("calculate-delta-temperature-button");
    const resultOutput = document.getElementById("delta-temperature-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_delta_temperature",
                data: {
                    sensible_heat: sensibleHeatInput.value || null,
                    specific_heat: specificHeatInput.value || null,
                    mass: massInput.value || null,
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
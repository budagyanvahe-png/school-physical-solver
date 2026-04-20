import { answerPhrase, errorPhrase, calculateEndpoint } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const sensibleHeatInput = document.getElementById("delta-temperature-sensible-heat");
    const specificHeatInput = document.getElementById("delta-temperature-specific-heat");
    const massInput = document.getElementById("delta-temperature-mass");
    const startTemperatureInput = document.getElementById("delta-temperature-start-temperature");
    const endTemperatureInput = document.getElementById("delta-temperature-end-temperature");
    const calculateButton = document.getElementById("calculate-delta-temperature-button");
    const resultOutput = document.getElementById("delta-temperature-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
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

document.addEventListener("DOMContentLoaded", function() {
    const specificFusionHeatInput = document.getElementById("fusion-heat-specific-fusion-heat");
    const massInput = document.getElementById("fusion-heat-mass");
    const calculateButton = document.getElementById("calculate-fusion-heat-button");
    const resultOutput = document.getElementById("fusion-heat-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_fusion_heat",
                data: {
                    specific_fusion_heat: specificFusionHeatInput.value || null,
                    mass: massInput.value || null,
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

document.addEventListener("DOMContentLoaded", function() {
    const specificHeatInput = document.getElementById("sensible-heat-specific-heat");
    const massInput = document.getElementById("sensible-heat-mass");
    const deltaTemperatureInput = document.getElementById("sensible-heat-delta-temperature");
    const startTemperatureInput = document.getElementById("sensible-heat-start-temperature");
    const endTemperatureInput = document.getElementById("sensible-heat-end-temperature");
    const calculateButton = document.getElementById("calculate-sensible-heat-button");
    const resultOutput = document.getElementById("sensible-heat-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
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

document.addEventListener("DOMContentLoaded", function() {
    const fusionHeatInput = document.getElementById("specific-fusion-heat-fusion-heat");
    const massInput = document.getElementById("specific-fusion-heat-mass");
    const calculateButton = document.getElementById("calculate-specific-fusion-heat-button");
    const resultOutput = document.getElementById("specific-fusion-heat-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_specific_fusion_heat",
                data: {
                    fusion_heat: fusionHeatInput.value || null,
                    mass: massInput.value || null,
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

document.addEventListener("DOMContentLoaded", function() {
    const sensibleHeatInput = document.getElementById("specific-heat-sensible-heat");
    const massInput = document.getElementById("specific-heat-mass");
    const deltaTemperatureInput = document.getElementById("specific-heat-delta-temperature");
    const startTemperatureInput = document.getElementById("specific-heat-start-temperature");
    const endTemperatureInput = document.getElementById("specific-heat-end-temperature");
    const calculateButton = document.getElementById("calculate-specific-heat-button");
    const resultOutput = document.getElementById("specific-heat-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
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
import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const massInput = document.getElementById("volume-mass");
    const densityInput = document.getElementById("volume-density");
    const totalForceInput = document.getElementById("volume-total-force");
    const accelerationInput = document.getElementById("volume-acceleration");
    const sensibleHeatInput = document.getElementById("volume-sensible-heat");
    const specificHeatInput = document.getElementById("volume-special-heat");
    const deltaTemperatureInput = document.getElementById("volume-delta-temperature");
    const startTemperatureInput = document.getElementById("volume-start-temperature");
    const endTemperatureInput = document.getElementById("volume-end-temperature");
    const kineticEnergyInput = document.getElementById("volume-kinetic-energy");
    const velocityInput = document.getElementById("volume-velocity");
    const potentialEnergyInput = document.getElementById("volume-potential-energy");
    const gravityAccelerationInput = document.getElementById("volume-gravity-acceleration");
    const heightInput = document.getElementById("volume-height");
    const fusionHeatInput = document.getElementById("volume-fusion-heat");
    const specificFusionHeatInput = document.getElementById("volume-specific-fusion-heat");
    const moleInput = document.getElementById("volume-mole");
    const molarMassInput = document.getElementById("volume-molar-mass");
    const calculateButton = document.getElementById("calculate-volume-button");
    const resultOutput = document.getElementById("volume-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_volume",
                data: {
                    mass: massInput.value || null,
                    density: densityInput.value || null,
                    total_force: totalForceInput.value || null,
                    acceleration: accelerationInput.value || null,
                    sensible_heat: sensibleHeatInput.value || null,
                    specific_heat: specificHeatInput.value || null,
                    delta_temperature: deltaTemperatureInput.value || null,
                    start_temperature: startTemperatureInput.value || null,
                    end_temperature: endTemperatureInput.value || null,
                    kinetic_energy: kineticEnergyInput.value || null,
                    velocity: velocityInput.value || null,
                    potential_energy: potentialEnergyInput.value || null,
                    gravity_acceleration: gravityAccelerationInput.value || null,
                    height: heightInput.value || null,
                    fusion_heat: fusionHeatInput.value || null,
                    specific_fusion_heat: specificFusionHeatInput.value || null,
                    mole: moleInput.value || null,
                    molar_mass: molarMassInput.value || null,
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
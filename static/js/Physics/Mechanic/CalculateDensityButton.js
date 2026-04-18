import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const massInput = document.getElementById("density-mass");
    const volumeInput = document.getElementById("density-volume");
    const totalForceInput = document.getElementById("density-total-force");
    const accelerationInput = document.getElementById("density-acceleration");
    const sensibleHeatInput = document.getElementById("density-sensible-heat");
    const specificHeatInput = document.getElementById("density-special-heat");
    const deltaTemperatureInput = document.getElementById("density-delta-temperature");
    const startTemperatureInput = document.getElementById("density-start-temperature");
    const endTemperatureInput = document.getElementById("density-end-temperature");
    const kineticEnergyInput = document.getElementById("density-kinetic-energy");
    const velocityInput = document.getElementById("density-velocity");
    const potentialEnergyInput = document.getElementById("density-potential-energy");
    const gravityAccelerationInput = document.getElementById("density-gravity-acceleration");
    const heightInput = document.getElementById("density-height");
    const fusionHeatInput = document.getElementById("density-fusion-heat");
    const specificFusionHeatInput = document.getElementById("density-specific-fusion-heat");
    const moleInput = document.getElementById("density-mole");
    const molarMassInput = document.getElementById("density-molar-mass");
    const calculateButton = document.getElementById("calculate-density-button");
    const resultOutput = document.getElementById("density-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_density",
                data: {
                    mass: massInput.value || null,
                    volume: volumeInput.value || null,
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
import { answerPhrase, errorPhrase } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const densityInput = document.getElementById("mass-density");
    const volumeInput = document.getElementById("mass-volume");
    const totalForceInput = document.getElementById("mass-total-force");
    const accelerationInput = document.getElementById("mass-acceleration");
    const sensibleHeatInput = document.getElementById("mass-sensible-heat");
    const specificHeatInput = document.getElementById("mass-special-heat");
    const deltaTemperatureInput = document.getElementById("mass-delta-temperature");
    const startTemperatureInput = document.getElementById("mass-start-temperature");
    const endTemperatureInput = document.getElementById("mass-end-temperature");
    const kineticEnergyInput = document.getElementById("mass-kinetic-energy");
    const velocityInput = document.getElementById("mass-velocity");
    const potentialEnergyInput = document.getElementById("mass-potential-energy");
    const gravityAccelerationInput = document.getElementById("mass-gravity-acceleration");
    const heightInput = document.getElementById("mass-height");
    const fusionHeatInput = document.getElementById("mass-fusion-heat");
    const specificFusionHeatInput = document.getElementById("mass-specific-fusion-heat");
    const moleInput = document.getElementById("mass-mole");
    const molarMassInput = document.getElementById("mass-molar-mass");
    const calculateButton = document.getElementById("calculate-mass-button");
    const resultOutput = document.getElementById("mass-result");

    calculateButton.addEventListener("click", function() {
        fetch("/calculate", {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_mass",
                data: {
                    density: densityInput.value || null,
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
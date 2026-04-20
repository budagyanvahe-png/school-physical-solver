import { errorPhrase, answerPhrase, calculateEndpoint } from "/static/js/config.js";

document.addEventListener("DOMContentLoaded", function() {
    const startVelocityInput = document.getElementById("acceleration-start-velocity");
    const endVelocityInput = document.getElementById("acceleration-end-velocity");
    const elapsedTimeInput = document.getElementById("acceleration-elapsed-time");
    const deltaVelocityInput = document.getElementById("acceleration-delta-velocity");
    const elapsedDistanceInput = document.getElementById("acceleration-elapsed-distance");
    const totalForceInput = document.getElementById("acceleration-total-force");
    const massInput = document.getElementById("acceleration-mass");
    const calculateButton = document.getElementById("calculate-acceleration-button");
    const resultOutput = document.getElementById("acceleration-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
            headers: {"Content-Type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_acceleration",
                data: {
                    start_velocity: startVelocityInput.value || null,
                    end_velocity: endVelocityInput.value || null,
                    elapsed_time: elapsedTimeInput.value || null,
                    delta_velocity: deltaVelocityInput.value || null,
                    elapsed_distance: elapsedDistanceInput.value || null,
                    total_force: totalForceInput.value || null,
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
    const densityInput = document.getElementById("archimedes-force-density");
    const gravityAccelerationInput = document.getElementById("archimedes-force-gravity-acceleration");
    const volumeInput = document.getElementById("archimedes-force-volume");
    const massInput = document.getElementById("archimedes-force-mass");
    const calculateButton = document.getElementById("calculate-archimedes-force-button");
    const resultOutput = document.getElementById("archimedes-force-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_archimedes_force",
                data: {
                    density: densityInput.value || null,
                    gravity_acceleration: gravityAccelerationInput.value || null,
                    volume: volumeInput.value || null,
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
    const startVelocityInput = document.getElementById("average-velocity-start-velocity");
    const endVelocityInput = document.getElementById("average-velocity-end-velocity");
    const deltaVelocityInput = document.getElementById("average-velocity-delta-velocity");
    const accelerationInput = document.getElementById("average-velocity-acceleration");
    const elapsedTimeInput = document.getElementById("average-velocity-elapsed-time");
    const calculateButton = document.getElementById("calculate-average-velocity-button");
    const resultOutput = document.getElementById("average-velocity-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_average_velocity",
                data: {
                    start_velocity: startVelocityInput.value || null,
                    end_velocity: endVelocityInput.value || null,
                    delta_velocity: deltaVelocityInput.value || null,
                    acceleration: accelerationInput.value || null,
                    elapsed_time: elapsedTimeInput.value || null,
                },
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
        fetch(calculateEndpoint, {
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

document.addEventListener("DOMContentLoaded", function() {
    const deltaVelocityInput = document.getElementById("end-velocity-delta-velocity");
    const startVelocityInput = document.getElementById("end-velocity-start-velocity");
    const accelerationInput = document.getElementById("end-velocity-acceleration");
    const elapsedDistanceInput = document.getElementById("end-velocity-elapsed-distance");
    const elapsedTimeInput = document.getElementById("end-velocity-elapsed-time");
    const averageVelocityInput = document.getElementById("end-velocity-average-velocity");
    const calculateButton = document.getElementById("calculate-end-velocity-button");
    const resultOutput = document.getElementById("end-velocity-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_end_velocity",
                data: {
                    delta_velocity: deltaVelocityInput.value || null,
                    start_velocity: startVelocityInput.value || null,
                    acceleration: accelerationInput.value || null,
                    elapsed_distance: elapsedDistanceInput.value || null,
                    elapsed_time: elapsedTimeInput.value || null,
                    average_velocity: averageVelocityInput.value || null,
                },
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
    const forceInput = document.getElementById("force-pressure-force");
    const areaInput = document.getElementById("force-pressure-area");
    const calculateButton = document.getElementById("calculate-force-pressure-button");
    const resultOutput = document.getElementById("force-pressure-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_force_pressure",
                data: {
                    force: forceInput.value || null,
                    area: areaInput.value || null,
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
    const slidingFrictionInput = document.getElementById("friction-force-sliding-friction");
    const supportReactionInput = document.getElementById("friction-force-support-reaction");
    const massInput = document.getElementById("friction-force-mass");
    const accelerationInput = document.getElementById("friction-force-acceleration");
    const angleInput = document.getElementById("friction-force-angle");
    const calculateButton = document.getElementById("calculate-friction-force-button");
    const resultOutput = document.getElementById("friction-force-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_friction_force",
                data: {
                    sliding_friction: slidingFrictionInput.value || null,
                    support_reaction: supportReactionInput.value || null,
                    mass: massInput.value || null,
                    acceleration: accelerationInput.value || null,
                    angle: angleInput.value || null,
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
    const densityInput = document.getElementById("hydrostatic-pressure-density");
    const gravityAccelerationInput = document.getElementById("hydrostatic-pressure-gravity-acceleration");
    const heightInput = document.getElementById("hydrostatic-pressure-height");
    const calculateButton = document.getElementById("calculate-hydrostatic-pressure-button");
    const resultOutput = document.getElementById("hydrostatic-pressure-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_hydrostatic_pressure",
                data: {
                    density: densityInput.value || null,
                    gravity_acceleration: gravityAccelerationInput.value || null,
                    height: heightInput.value || null,
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
    const massInput = document.getElementById("kinetic-energy-mass");
    const velocityInput = document.getElementById("kinetic-energy-velocity");
    const impulseInput = document.getElementById("kinetic-energy-impulse");
    const calculateButton = document.getElementById("calculate-kinetic-energy-button");
    const resultOutput = document.getElementById("kinetic-energy-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_kinetic_energy",
                data: {
                    mass: massInput.value || null,
                    velocity: velocityInput.value || null,
                    impulse: impulseInput.value || null,
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
        fetch(calculateEndpoint, {
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

document.addEventListener("DOMContentLoaded", function() {
    const totalForceInput = document.getElementById("mechanical-work-total-force");
    const elapsedDistanceInput = document.getElementById("mechanical-work-elapsed-distance");
    const angleInput = document.getElementById("mechanical-work-angle");
    const startKineticEnergy = document.getElementById("mechanical-work-start-kinetic-energy");
    const endKineticEnergy = document.getElementById("mechanical-work-end-kinetic-energy");
    const calculateButton = document.getElementById("calculate-mechanical-work-button");
    const resultOutput = document.getElementById("mechanical-work-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_mechanical_work",
                data: {
                    total_force: totalForceInput.value || null,
                    elapsed_distance: elapsedDistanceInput.value || null,
                    angle: angleInput.value || null,
                    start_kinetic_energy: startKineticEnergy.value || null,
                    end_kinetic_energy: endKineticEnergy.value || null,
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
    const massInput = document.getElementById("potential-energy-mass");
    const accelerationInput = document.getElementById("potential-energy-acceleration");
    const heightInput = document.getElementById("potential-energy-height");
    const hardnessInput = document.getElementById("potential-energy-hardness");
    const startLengthInput = document.getElementById("potential-energy-start-length");
    const endLengthInput = document.getElementById("potential-energy-end-length");
    const deltaLengthInput = document.getElementById("potential-energy-delta-length");
    const calculateButton = document.getElementById("calculate-potential-energy-button");
    const resultOutput = document.getElementById("potential-energy-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_potential_energy",
                data: {
                    mass: massInput.value || null,
                    acceleration: accelerationInput.value || null,
                    height: heightInput.value || null,
                    hardness: hardnessInput.value || null,
                    start_length: startLengthInput.value || null,
                    end_length: endLengthInput.value || null,
                    delta_length: deltaLengthInput.value || null,
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
    const deltaVelocityInput = document.getElementById("start-velocity-delta-velocity");
    const endVelocityInput = document.getElementById("start-velocity-end-velocity");
    const accelerationInput = document.getElementById("start-velocity-acceleration");
    const elapsedTimeInput = document.getElementById("start-velocity-elapsed-time");
    const elapsedDistanceInput = document.getElementById("start-velocity-elapsed-distance");
    const averageVelocityInput = document.getElementById("start-velocity-average-velocity");
    const calculateButton = document.getElementById("calculate-start-velocity-button");
    const resultOutput = document.getElementById("start-velocity-result");

    calculateButton.addEventListener("click", function() {
        fetch(calculateEndpoint, {
            headers: {"Content-type": "application/json"},
            method: "POST",
            body: JSON.stringify({
                formula_type: "get_start_velocity",
                data: {
                    delta_velocity: deltaVelocityInput.value || null,
                    end_velocity: endVelocityInput.value || null,
                    acceleration: accelerationInput.value || null,
                    elapsed_time: elapsedTimeInput.value || null,
                    elapsed_distance: elapsedDistanceInput.value || null,
                    average_velocity: averageVelocityInput.value || null,
                },
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
        fetch(calculateEndpoint, {
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
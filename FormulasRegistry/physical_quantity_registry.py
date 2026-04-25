from typing import Callable
from Physics.Electricity import get_dissipated_heat, get_voltage, get_current, get_resistance, get_electrical_power
from Physics.Mechanic import get_friction_force, get_mechanical_work, get_kinetic_energy, get_potential_energy, get_full_mechanic_energy
from Physics.Mechanic import get_acceleration, get_start_velocity, get_average_velocity, get_end_velocity
from Physics.Mechanic import get_density, get_volume, get_mass, get_force_pressure, get_hydrostatic_pressure, get_archimedes_force
from Physics.Thermodynamic import get_sensible_heat, get_specific_heat, get_delta_temperature, get_specific_fusion_heat, get_fusion_heat

physical_quantity_map: dict[str, Callable] = {
    "get_dissipated_heat": get_dissipated_heat,
    "get_voltage": get_voltage,
    "get_current": get_current,
    "get_resistance": get_resistance,
    "get_electrical_power": get_electrical_power,

    "get_friction_force": get_friction_force,
    "get_mechanical_work": get_mechanical_work,
    "get_kinetic_energy": get_kinetic_energy,
    "get_potential_energy": get_potential_energy,
    "get_full_mechanic_energy": get_full_mechanic_energy,
    "get_acceleration": get_acceleration,
    "get_start_velocity": get_start_velocity,
    "get_average_velocity": get_average_velocity,
    "get_end_velocity": get_end_velocity,
    "get_density": get_density,
    "get_volume": get_volume,
    "get_mass": get_mass,
    "get_force_pressure": get_force_pressure,
    "get_hydrostatic_pressure": get_hydrostatic_pressure,
    "get_archimedes_force": get_archimedes_force,
    
    "get_sensible_heat": get_sensible_heat,
    "get_specific_heat": get_specific_heat,
    "get_delta_temperature": get_delta_temperature,
    "get_specific_fusion_heat": get_specific_fusion_heat,
    "get_fusion_heat": get_fusion_heat,
}
from utils import validate_value_type, get_first_value_with_given_type_from_iterator, trim_trailing_zeros
from decimal import Decimal
from math import sqrt

def get_dissipated_heat(*,
                        current: str | None = None,
                        resistance: str | None = None,
                        elapsed_time: str | None = None,
                        voltage: str | None = None,
                        electrical_power: str | None = None,
                        ) -> str | None:
    
    def by_current_and_resistance_and_elapsed_time(*,
                                                   current: str | None,
                                                   resistance: str | None,
                                                   elapsed_time: str | None,
                                                   ) -> str | None:
        
        try:
            validated_current: str = validate_value_type(value=current, value_type=(str,))
            validated_resistance: str = validate_value_type(value=resistance, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            decimal_result: Decimal = (Decimal(value=validated_current) ** 2) * Decimal(value=validated_resistance) * Decimal(value=validated_elapsed_time)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_voltage_and_current_and_elapsed_time(*,
                                                voltage: str | None,
                                                current: str | None,
                                                elapsed_time: str | None,
                                                ) -> str | None:
        
        try:
            validated_voltage: str = validate_value_type(value=voltage, value_type=(str,))
            validated_current: str = validate_value_type(value=current, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_voltage) * Decimal(value=validated_current) * Decimal(value=validated_elapsed_time)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_electrical_power_and_elapsed_time(*,
                                     electrical_power: str | None,
                                     elapsed_time: str | None,
                                     ) -> str | None:
        
        try:
            validated_electrical_power: str = validate_value_type(value=electrical_power, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_electrical_power) * Decimal(value=validated_elapsed_time)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    solution_by_current_and_resistance_and_elapsed_time: str | None = by_current_and_resistance_and_elapsed_time(current=current,
                                                                                                                   resistance=resistance,
                                                                                                                   elapsed_time=elapsed_time,
                                                                                                                   )
    
    solution_by_voltage_and_current_and_elapsed_time: str | None = by_voltage_and_current_and_elapsed_time(voltage=voltage,
                                                                                                             current=current,
                                                                                                             elapsed_time=elapsed_time,
                                                                                                             )
    
    solution_by_electrical_power_and_elapsed_time: str | None = by_electrical_power_and_elapsed_time(electrical_power=electrical_power,
                                                                                                       elapsed_time=elapsed_time,
                                                                                                       )
    
    solution_list: list[str | None] = [
        solution_by_current_and_resistance_and_elapsed_time,
        solution_by_voltage_and_current_and_elapsed_time,
        solution_by_electrical_power_and_elapsed_time,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_voltage(*,
                current: str | None = None,
                resistance: str | None = None,
                dissipated_heat: str | None = None,
                elapsed_time: str | None = None,
                electrical_power: str | None = None,
                ) -> str | None:
    
    def by_current_and_resistance(*,
                                  current: str | None,
                                  resistance: str | None,
                                  ) -> str | None:
        
        try:
            validated_current: str = validate_value_type(value=current, value_type=(str,))
            validated_resistance: str = validate_value_type(value=resistance, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_current) * Decimal(value=validated_resistance)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_dissipated_heat_and_current_and_elapsed_time(*,
                                                        dissipated_heat: str | None,
                                                        current: str | None,
                                                        elapsed_time: str | None,
                                                        ) -> str | None:
        
        try:
            validated_dissiapated_heat: str = validate_value_type(value=dissipated_heat, value_type=(str,))
            validated_current: str = validate_value_type(value=current, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_dissiapated_heat) / (Decimal(value=validated_current) * Decimal(value=validated_elapsed_time))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_electrical_power_and_current(*,
                                      electrical_power: str | None,
                                      current: str | None,
                                      ) -> str | None:
        
        try:
            validated_electrical_power: str = validate_value_type(value=electrical_power, value_type=(str,))
            validated_current: str = validate_value_type(value=current, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_electrical_power) / Decimal(value=validated_current)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    solution_by_current_and_resistance: str | None = by_current_and_resistance(current=current, 
                                                                                 resistance=resistance
                                                                                 )

    solution_by_dissipated_heat_and_current_and_elapsed_time: str | None = by_dissipated_heat_and_current_and_elapsed_time(dissipated_heat=dissipated_heat,
                                                                                                                             current=current,
                                                                                                                             elapsed_time=elapsed_time,
                                                                                                                             )

    solution_by_electrical_power_and_current: str | None = by_electrical_power_and_current(electrical_power=electrical_power,
                                                                                         current=current,
                                                                                         )
    
    solution_list: list[str | None] = [
        solution_by_current_and_resistance,
        solution_by_dissipated_heat_and_current_and_elapsed_time,
        solution_by_electrical_power_and_current,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_current(*,
                voltage: str | None = None,
                resistance: str | None = None,
                dissipated_heat: str | None = None,
                elapsed_time: str | None = None,
                electrical_power: str | None = None,
                ) -> str | None:
    
    def by_voltage_and_resistance(*,
                                  voltage: str | None,
                                  resistance: str | None,
                                  ) -> str | None:
        
        try:
            validated_voltage: str = validate_value_type(value=voltage, value_type=(str,))
            validated_resistance: str = validate_value_type(value=resistance, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_voltage) / Decimal(value=validated_resistance)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_dissipated_heat_and_resistance_and_elapsed_time(*,
                                                           dissipated_heat: str | None,
                                                           resistance: str | None,
                                                           elapsed_time: str | None,
                                                           ) -> str | None:
        
        try:
            validated_dissipated_heat: str = validate_value_type(value=dissipated_heat, value_type=(str,))
            validated_resistance: str = validate_value_type(value=resistance, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            decimal_result: Decimal = Decimal(value=sqrt(Decimal(value=validated_dissipated_heat) / (Decimal(value=validated_resistance) * Decimal(value=validated_elapsed_time))))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
    
    def by_dissipated_heat_and_voltage_and_elapsed_time(*,
                                                        dissipated_heat: str | None,
                                                        voltage: str | None,
                                                        elapsed_time: str | None,
                                                        ) -> str | None:
        
        try:
            validated_dissipated_heat: str = validate_value_type(value=dissipated_heat, value_type=(str,))
            validated_voltage: str = validate_value_type(value=voltage, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_dissipated_heat) / (Decimal(value=validated_voltage) * Decimal(value=validated_elapsed_time))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
    
    def by_electrical_power_and_voltage(*,
                                      electrical_power: str | None,
                                      voltage: str | None,
                                      ) -> str | None:
        
        try:
            validated_electrical_power: str = validate_value_type(value=electrical_power, value_type=(str,))
            validated_voltage: str = validate_value_type(value=voltage, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_electrical_power) / Decimal(value=validated_voltage)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    solution_by_voltage_and_resistance: str | None = by_voltage_and_resistance(voltage=voltage,
                                                                                 resistance=resistance
                                                                                 )

    solution_by_dissipated_heat_and_resistance_and_elapsed_time: str | None = by_dissipated_heat_and_resistance_and_elapsed_time(dissipated_heat=dissipated_heat,
                                                                                                                                   resistance=resistance,
                                                                                                                                   elapsed_time=elapsed_time,
                                                                                                                                   )

    solution_by_dissipated_heat_and_voltage_and_elapsed_time: str | None = by_dissipated_heat_and_voltage_and_elapsed_time(dissipated_heat=dissipated_heat,
                                                                                                                             voltage=voltage,
                                                                                                                             elapsed_time=elapsed_time,
                                                                                                                             )

    solution_by_electrical_power_and_voltage: str | None = by_electrical_power_and_voltage(electrical_power=electrical_power,
                                                                                         voltage=voltage,
                                                                                         )

    solution_list: list[str | None] = [
        solution_by_voltage_and_resistance,
        solution_by_dissipated_heat_and_resistance_and_elapsed_time,
        solution_by_dissipated_heat_and_voltage_and_elapsed_time,
        solution_by_electrical_power_and_voltage,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_resistance(*,
                   voltage: str | None = None,
                   current: str | None = None,
                   dissipated_heat: str | None = None,
                   elapsed_time: str | None = None,
                   electrical_power: str | None = None,
                   specific_resistance: str | None = None,
                   electrical_conductor_length: str | None = None,
                   conductor_transverse_area: str | None = None,
                   ) -> str | None:
    
    def by_voltage_and_current(*,
                               voltage: str | None,
                               current: str | None,
                               ) -> str | None:
        
        try:
            validated_voltage: str = validate_value_type(value=voltage, value_type=(str,))
            validated_current: str = validate_value_type(value=current, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_voltage) / Decimal(value=validated_current)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_specific_resistance_and_electrical_conductor_length_and_conductor_transverse_area(*,
                                                                                                      specific_material_resistance: str | None,
                                                                                                      electrical_conductor_length: str | None,
                                                                                                      conductor_transverse_area: str | None,
                                                                                                      ) -> str | None:
        
        try:
            validated_specific_resistance: str = validate_value_type(value=specific_material_resistance, value_type=(str,)) / 1_000_000
            validated_electrical_conductor_length: str = validate_value_type(value=electrical_conductor_length, value_type=(str,))
            validated_conductor_transverse_area: str = validate_value_type(value=conductor_transverse_area, value_type=(str,)) / 1_000_000

            decimal_result: Decimal = (Decimal(value=validated_specific_resistance) * Decimal(value=validated_electrical_conductor_length)) / Decimal(value=validated_conductor_transverse_area)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_dissipated_heat_and_current_and_elapsed_time(*,
                                                        dissipated_heat: str | None,
                                                        current: str | None,
                                                        elapsed_time: str | None,
                                                        ) -> str | None:
        
        try:
            validated_dissipated_heat: str = validate_value_type(value=dissipated_heat, value_type=(str,))
            validated_current: str = validate_value_type(value=current, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_dissipated_heat) / (Decimal(value=validated_current) * Decimal(value=validated_elapsed_time))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_electrical_power_and_current(*,
                                        electrical_power: str | None,
                                        current: str | None,
                                        ) -> str | None:
        
        try:
            validated_electrical_power: str = validate_value_type(value=electrical_power, value_type=(str,))
            validated_current: str = validate_value_type(value=current, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_electrical_power) / (Decimal(value=validated_current) ** 2)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    solution_by_voltage_and_current: str | None = by_voltage_and_current(voltage=voltage,
                                                                           current=current,
                                                                           )
    
    solution_by_specific_resistance_and_electrical_conductor_length_and_conductor_transverse_area: str | None = by_specific_resistance_and_electrical_conductor_length_and_conductor_transverse_area(specific_material_resistance=specific_resistance,
                                                                                                                                                                                                                         electrical_conductor_length=electrical_conductor_length,
                                                                                                                                                                                                                         conductor_transverse_area=conductor_transverse_area,
                                                                                                                                                                                                                         )

    solution_by_dissipated_heat_and_current_and_elapsed_time: str | None = by_dissipated_heat_and_current_and_elapsed_time(dissipated_heat=dissipated_heat,
                                                                                                                             current=current,
                                                                                                                             elapsed_time=elapsed_time,
                                                                                                                             )
    
    solution_by_electrical_power_and_current: str | None = by_electrical_power_and_current(electrical_power=electrical_power,
                                                                                             current=current
                                                                                             )
                                                                                                                                                                                                                         
    solution_list: list[str | None] = [
        solution_by_voltage_and_current,
        solution_by_specific_resistance_and_electrical_conductor_length_and_conductor_transverse_area,
        solution_by_dissipated_heat_and_current_and_elapsed_time,
        solution_by_electrical_power_and_current,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_electrical_power(*,
                         voltage: str | None = None,
                         current: str | None = None,
                         resistance: str | None = None,
                         dissipated_heat: str | None = None,
                         elapsed_time: str | None = None,
                         ) -> str | None:
    
    def by_voltage_and_current(*,
                               voltage: str | None,
                               current: str | None,
                               ) -> str | None:
        
        try:
            validated_voltage: str = validate_value_type(value=voltage, value_type=(str,))
            validated_current: str = validate_value_type(value=current, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_voltage) * Decimal(value=validated_current)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_current_and_resistance(*,
                                  current: str | None,
                                  resistance: str | None,
                                  ) -> str | None:
        
        try:
            validated_current: str = validate_value_type(value=current, value_type=(str,))
            validated_resistance: str = validate_value_type(value=resistance, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_current) ** 2 * Decimal(value=validated_resistance)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_dissipated_heat_and_elapsed_time(*,
                                            dissipated_heat: str | None,
                                            elapsed_time: str | None,
                                            ) -> str | None:
        
        try:
            validated_dissipated_heat: str = validate_value_type(value=dissipated_heat, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_dissipated_heat) / Decimal(value=validated_elapsed_time)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    solution_by_voltage_and_current: str | None = by_voltage_and_current(voltage=voltage,
                                                                           current=current,
                                                                           )
    
    solution_by_current_and_resistance: str | None = by_current_and_resistance(current=current,
                                                                                 resistance=resistance,
                                                                                 )
    
    solution_by_dissipated_heat_and_elapsed_time: str | None = by_dissipated_heat_and_elapsed_time(dissipated_heat=dissipated_heat,
                                                                                                     elapsed_time=elapsed_time,
                                                                                                     )
    
    solution_list: list[str | None] = [
        solution_by_voltage_and_current,
        solution_by_current_and_resistance,
        solution_by_dissipated_heat_and_elapsed_time,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(Decimal, str))
    return result

#Approved
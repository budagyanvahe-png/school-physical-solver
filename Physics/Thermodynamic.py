from utils import validate_value_type, get_first_value_with_given_type_from_iterator, trim_trailing_zeros
from decimal import Decimal

def get_sensible_heat(*,
                      specific_heat: str | None = None,
                      mass: str | None = None,
                      delta_temperature: str | None = None,
                      start_temperature: str | None = None,
                      end_temperature: str | None = None,
                      ) -> str | None:

    def by_specific_heat_and_mass_and_delta_temperature(*,
                                                                 specific_heat: str | None,
                                                                 mass: str | None,
                                                                 delta_temperature: str | None,
                                                                 ) -> str | None:
        
        try:
            validated_specific_heat: str = validate_value_type(value=specific_heat, value_type=(str,))
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))
            validated_delta_temperature: str = validate_value_type(value=delta_temperature, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_specific_heat) * Decimal(value=validated_mass) * Decimal(value=validated_delta_temperature)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_specific_heat_and_mass_and_start_temperature_and_end_temperature(*,
                                                                                     specific_heat: str | None,
                                                                                     mass: str | None,
                                                                                     start_temperature: str | None,
                                                                                     end_temperature: str | None,
                                                                                     ) -> str | None:
        
        try:
            validated_specific_heat: str = validate_value_type(value=specific_heat, value_type=(str,))
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))
            validated_start_temperature: str = validate_value_type(value=start_temperature, value_type=(str,))
            validated_end_temperature: str = validate_value_type(value=end_temperature, value_type=(str,))

            validated_delta_temperature: Decimal = Decimal(value=validated_end_temperature) - Decimal(value=validated_start_temperature)

            decimal_result: Decimal = Decimal(value=validated_specific_heat) * Decimal(value=validated_mass) * validated_delta_temperature
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    solution_by_specific_heat_and_mass_and_delta_temperature: str | None = by_specific_heat_and_mass_and_delta_temperature(specific_heat=specific_heat,
                                                                                                                                               mass=mass,
                                                                                                                                               delta_temperature=delta_temperature,
                                                                                                                                               )

    solution_by_specific_heat_and_mass_and_start_temperature_and_end_temperature: str | None = by_specific_heat_and_mass_and_start_temperature_and_end_temperature(specific_heat=specific_heat,
                                                                                                                                                                                       mass=mass,
                                                                                                                                                                                       start_temperature=start_temperature,
                                                                                                                                                                                       end_temperature=end_temperature,
                                                                                                                                                                                       )

    solution_list: list[str | None] = [
        solution_by_specific_heat_and_mass_and_delta_temperature,
        solution_by_specific_heat_and_mass_and_start_temperature_and_end_temperature,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_specific_heat(*,
                      sensible_heat: str | None = None,
                      mass: str | None = None,
                      delta_temperature: str | None = None,
                      start_temperature: str | None = None,
                      end_temperature: str | None = None,
                      ) -> str | None:
    
    def by_sensible_heat_and_mass_and_delta_temperature(*, 
                                                        sensible_heat: str | None,
                                                        mass: str | None,
                                                        delta_temperature: str | None,
                                                        ) -> str | None:
        
        try:
            validated_sensible_heat: str = validate_value_type(value=sensible_heat, value_type=(str,))
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))
            validated_delta_temperature: str = validate_value_type(value=delta_temperature, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_sensible_heat) / (Decimal(value=validated_mass) * Decimal(value=validated_delta_temperature))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_sensible_heat_and_mass_and_start_temperature_and_end_temperature(*,
                                                                            sensible_heat: str | None,
                                                                            mass: str | None,
                                                                            start_temperature: str | None,
                                                                            end_temperature: str | None,
                                                                            ) -> str | None:
        
        try:
            validated_sensible_heat: str = validate_value_type(value=sensible_heat, value_type=(str,))
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))
            validated_start_temperature: str = validate_value_type(value=start_temperature, value_type=(str,))
            validated_end_temperature: str = validate_value_type(value=end_temperature, value_type=(str,))

            validated_delta_temperature: Decimal = Decimal(value=validated_end_temperature) - Decimal(value=validated_start_temperature)

            decimal_result: Decimal = Decimal(value=validated_sensible_heat) / (Decimal(value=validated_mass) * validated_delta_temperature)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    solution_by_sensible_heat_and_mass_and_delta_temperature: str | None = by_sensible_heat_and_mass_and_delta_temperature(sensible_heat=sensible_heat,
                                                                                                                             mass=mass,
                                                                                                                             delta_temperature=delta_temperature,
                                                                                                                             )
    
    solution_by_sensible_heat_and_mass_and_start_temperature_and_end_temperature: str | None = by_sensible_heat_and_mass_and_start_temperature_and_end_temperature(sensible_heat=sensible_heat,
                                                                                                                                                                     mass=mass,
                                                                                                                                                                     start_temperature=start_temperature,
                                                                                                                                                                     end_temperature=end_temperature,
                                                                                                                                                                     )
    
    solution_list: list[str | None] = [
        solution_by_sensible_heat_and_mass_and_delta_temperature,
        solution_by_sensible_heat_and_mass_and_start_temperature_and_end_temperature
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_delta_temperature(*,
                          sensible_heat: str | None = None,
                          specific_heat: str | None = None,
                          mass: str | None = None,
                          start_temperature: str | None = None,
                          end_temperature: str | None = None,
                          ) -> str | None:
    
    def by_sensible_heat_and_specific_heat_and_mass(*,
                                                             sensible_heat: str | None,
                                                             specific_heat: str | None,
                                                             mass: str | None,
                                                             ) -> str | None:
        
        try:
            validated_sensible_heat: str = validate_value_type(value=sensible_heat, value_type=(str,))
            validated_specific_heat: str = validate_value_type(value=specific_heat, value_type=(str,))
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_sensible_heat) / (Decimal(value=validated_specific_heat) * Decimal(value=validated_mass))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_start_temperature_and_end_temperature(*,
                                                 start_temperature: str | None,
                                                 end_temperature: str | None,
                                                 ) -> str | None:
        
        try:
            validated_start_temperature: str = validate_value_type(value=start_temperature, value_type=(str,))
            validated_end_temperature: str = validate_value_type(value=end_temperature, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_end_temperature) - Decimal(value=validated_start_temperature)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    solution_by_sensible_heat_and_specific_heat_and_mass: str | None = by_sensible_heat_and_specific_heat_and_mass(sensible_heat=sensible_heat,
                                                                                                                                       specific_heat=specific_heat,
                                                                                                                                       mass=mass,
                                                                                                                                       )
    
    solution_by_start_temperature_and_end_temperature: str | None = by_start_temperature_and_end_temperature(start_temperature=start_temperature,
                                                                                                               end_temperature=end_temperature,
                                                                                                               )
    
    solution_list: list[str | None] = [
        solution_by_sensible_heat_and_specific_heat_and_mass,
        solution_by_start_temperature_and_end_temperature,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_specific_fusion_heat(*,
                             fusion_heat: str | None = None,
                             mass: str | None = None,
                             ) -> str | None:
    
    def by_fusion_heat_and_mass(*,
                                fusion_heat: str | None,
                                mass: str | None,
                                ) -> str | None:
    
        try:
            validated_fusion_heat: str = validate_value_type(value=fusion_heat, value_type=(str,))
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_fusion_heat) / Decimal(value=validated_mass)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    solution_by_fusion_heat_and_mass: str | None = by_fusion_heat_and_mass(fusion_heat=fusion_heat,
                                                                           mass=mass,
                                                                           )
    
    solution_list: list[str | None] = [
        solution_by_fusion_heat_and_mass,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result
    
def get_fusion_heat(*,
                    specific_fusion_heat: str | None = None,
                    mass: str | None = None,
                    ) -> str | None:
    
    def by_specific_fusion_heat_and_mass(*,
                                         specific_fusion_heat: str | None,
                                         mass: str | None,
                                         ) -> str | None:
    
        try:
            validated_specific_fusion_heat: str = validate_value_type(value=specific_fusion_heat, value_type=(str,))
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_specific_fusion_heat) * Decimal(value=validated_mass)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    solution_by_specific_fusion_heat_and_mass: str | None = by_specific_fusion_heat_and_mass(specific_fusion_heat=specific_fusion_heat,
                                                                                             mass=mass,
                                                                                             )
    
    solution_list: list[str | None] = [
        solution_by_specific_fusion_heat_and_mass,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

#Approved
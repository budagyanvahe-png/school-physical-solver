from utils import validate_value_type, get_first_value_with_given_type_from_iterator, trim_trailing_zeros
from decimal import Decimal
from math import cos, radians

#Formulas of Dynamic

def get_friction_force(*,
                      sliding_friction: str | None = None,
                      support_reaction: str | None = None,

                      mass: str | None = None,
                      acceleration: str | None = None,
                      angle: str| None = "0.0",

                      ) -> str | None:
    
    def by_sliding_friction_and_support_reaction(*,
                                                 sliding_friction: str | None,
                                                 support_reaction: str | None,
                                                 ) -> str | None:
    
        try:
            validated_sliding_friction: str = validate_value_type(value=sliding_friction, value_type=(str,))
            validated_support_reaction: str = validate_value_type(value=support_reaction, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_sliding_friction) * Decimal(value=validated_support_reaction)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_mass_and_acceleration_and_angle(*,
                                           mass: str | None,
                                           acceleration: str | None,
                                           angle: str | None,
                                           ) -> str | None:
        
        try:
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))
            validated_acceleration: str = validate_value_type(value=acceleration, value_type=(str,))
            validated_angle: str = validate_value_type(value=angle, value_type=(str,))

            actual_angle: Decimal = Decimal(value=str(cos(radians(float(validated_angle)))))

            decimal_result: Decimal = Decimal(value=validated_mass) * Decimal(value=validated_acceleration) * actual_angle
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
    
    solution_by_sliding_friction_and_support_reaction: str | None = by_sliding_friction_and_support_reaction(sliding_friction=sliding_friction,
                                                                                                               support_reaction=support_reaction,
                                                                                                               )
    
    solution_by_mass_and_acceleration_and_angle: str | None = by_mass_and_acceleration_and_angle(mass=mass,
                                                                                                   acceleration=acceleration,
                                                                                                   angle=angle,
                                                                                                   )
    
    solution_list: list[str | None] = [
        solution_by_sliding_friction_and_support_reaction,
        solution_by_mass_and_acceleration_and_angle,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_mechanical_work(*, 
                        total_force: str | None = None,
                        elapsed_distance: str | None,
                        angle: str| None = "0.0",

                        start_kinetic_energy: str | None = None,
                        end_kinetic_energy: str | None = None,

                        ) -> str | None:
    
    def by_total_force_and_elapsed_distance_and_angle(*,
                                                total_force: str | None,
                                                elapsed_distance: str | None,
                                                angle: str | None,
                                                ) -> str | None:
        
        try:
            validated_total_force: str = validate_value_type(value=total_force, value_type=(str,))
            validated_elapsed_distance: str = validate_value_type(value=elapsed_distance, value_type=(str,))
            validated_angle: str = validate_value_type(value=angle, value_type=(str,))

            actual_angle = Decimal(value=str(cos(radians(float(validated_angle)))))

            decimal_result: Decimal = Decimal(value=validated_total_force) * Decimal(value=validated_elapsed_distance) * actual_angle
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_start_kinetic_energy_and_end_kinetic_energy(*,
                                                       start_kinetic_energy: str | None,
                                                       end_kinetic_energy: str | None,
                                                       ) -> str | None:
        
        try:
            validated_start_kinetic_energy: str = validate_value_type(value=start_kinetic_energy, value_type=(str,))
            validated_end_kinetic_energy: str = validate_value_type(value=end_kinetic_energy, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_end_kinetic_energy) - Decimal(value=validated_start_kinetic_energy)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    solution_by_total_force_and_elapsed_distance_and_angle: str | None = by_total_force_and_elapsed_distance_and_angle(total_force=total_force, 
                                                                                                             elapsed_distance=elapsed_distance, 
                                                                                                             angle=angle
                                                                                                             )
    
    solution_by_start_kinetic_energy_and_end_kinetic_energy: str | None = by_start_kinetic_energy_and_end_kinetic_energy(start_kinetic_energy=start_kinetic_energy,
                                                                                                                           end_kinetic_energy=end_kinetic_energy,
                                                                                                                           )

    solution_list: list[str | None] = [
        solution_by_total_force_and_elapsed_distance_and_angle,
        solution_by_start_kinetic_energy_and_end_kinetic_energy,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_kinetic_energy(*,
                       mass: str | None = None,
                       velocity: str | None = None,

                       impulse: str | None = None,
                       ) -> str | None:

    def by_mass_and_velocity(*,
                             mass: str | None,
                             velocity: str | None,
                             ) -> str | None:
    
        try:
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))
            validated_velocity: str = validate_value_type(value=velocity, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_mass) * (Decimal(value=validated_velocity) ** 2) / 2
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_impulse_and_mass(*,
                            impulse: str | None,
                            mass: str | None,
                            ) -> str | None:
        
        try:
            validated_impulse: str = validate_value_type(value=impulse, value_type=(str,))
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))

            decimal_result: Decimal = (Decimal(value=validated_impulse) ** 2) / (Decimal(value=validated_mass) * 2)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    solution_by_mass_and_velocity: str | None = by_mass_and_velocity(mass=mass,
                                                                       velocity=velocity,
                                                                       )
    
    solution_by_impulse_and_mass: str | None = by_impulse_and_mass(impulse=impulse,
                                                                     mass=mass,
                                                                     )
    
    solution_list: list[str | None] = [
        solution_by_mass_and_velocity,
        solution_by_impulse_and_mass,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result
    
def get_potential_energy(*,
                         mass: str | None = None,
                         acceleration: str | None = None,
                         height: str | None = None,

                         hardness: str | None = None,
                         start_length: str | None = None,
                         end_length: str | None = None,
                         delta_length: str | None = None,

                         ) -> str | None:
    
    def by_mass_and_acceleration_and_height(*,
                                            mass: str | None,
                                            acceleration: str | None,
                                            height: str | None,
                                            ) -> str | None:
    
        try:
            validated_mass: str= validate_value_type(value=mass, value_type=(str,))
            validated_acceleration: str = validate_value_type(value=acceleration, value_type=(str,))
            validated_height: str = validate_value_type(value=height, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_mass) * Decimal(value=validated_acceleration) * Decimal(value=validated_height)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_hardness_and_start_length_and_end_length(*,
                                                    hardness: str | None,
                                                    start_length: str | None,
                                                    end_length: str | None,
                                                    ) -> str | None:
        
        try:
            validated_hardness: str = validate_value_type(value=hardness, value_type=(str,))
            validated_start_length: str = validate_value_type(value=start_length, value_type=(str,))
            validated_end_length: str = validate_value_type(value=end_length, value_type=(str,))

            validated_delta_length: Decimal = Decimal(value=validated_end_length) - Decimal(value=validated_start_length)

            decimal_result: Decimal = Decimal(value=validated_hardness) * (validated_delta_length ** 2) / 2
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_hardness_and_delta_length(*,
                                     hardness: str | None,
                                     delta_length: str | None,
                                     ) -> str | None:
        
        try:
            validated_hardness: str = validate_value_type(value=hardness, value_type=(str,))
            validated_delta_length: str = validate_value_type(value=delta_length, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_hardness) * (Decimal(value=validated_delta_length) ** 2) / 2
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    solution_by_mass_and_acceleration_and_height: str | None = by_mass_and_acceleration_and_height(mass=mass,
                                                                                                           acceleration=acceleration,
                                                                                                           height=height,
                                                                                                           )
    
    solution_by_hardness_and_start_length_and_end_length: str | None = by_hardness_and_start_length_and_end_length(hardness=hardness,
                                                                                                                     start_length=start_length,
                                                                                                                     end_length=end_length,
                                                                                                                     )
    
    solution_by_hardness_and_delta_length: str | None = by_hardness_and_delta_length(hardness=hardness,
                                                                                       delta_length=delta_length,
                                                                                       )
    
    solution_list: list[str | None] = [
        solution_by_mass_and_acceleration_and_height,
        solution_by_hardness_and_start_length_and_end_length,
        solution_by_hardness_and_delta_length,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result
    
def get_full_mechanic_energy(*,
                             mass: str | None = None,
                             velocity: str | None = None,
                             acceleration: str | None = None,
                             height: str | None = None,
                             ) -> str | None:
    
    def get_kinetic_part(*,
                         mass: str | None,
                         velocity: str | None,
                         ) -> str | None:
        
        try:
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))
            validated_velocity: str = validate_value_type(value=velocity, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_mass) * (Decimal(value=validated_velocity) ** 2) / 2
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def get_potential_part(*,
                           mass: str | None,
                           acceleration: str | None,
                           height: str | None,
                           ) -> str | None:
        
        try:
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))
            validated_acceleration: str = validate_value_type(value=acceleration, value_type=(str,))
            validated_height: str = validate_value_type(value=height, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_mass) * Decimal(value=validated_acceleration) * Decimal(value=validated_height)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    try:
        kinetic_part: str | None = get_kinetic_part(mass=mass, 
                                                      velocity=velocity,
                                                      )
        
        potential_part: str | None = get_potential_part(mass=mass, 
                                                          acceleration=acceleration, 
                                                          height=height,
                                                          )
        
        validated_kinetic_part: str = validate_value_type(value=kinetic_part, value_type=(str,))
        validated_potential_part: str = validate_value_type(value=potential_part, value_type=(str,))

        result: str = validated_kinetic_part + validated_potential_part
        return result
    except TypeError:
        return None
    
#Formulas of Kinematic

def get_acceleration(*,
                     start_velocity: str | None,
                     end_velocity: str | None,
                     elapsed_time: str | None,
                     delta_velocity: str | None,
                     elapsed_distance: str | None,
                     total_force: str | None,
                     mass: str | None,
                     ) -> str | None:
    
    def by_start_velocity_and_end_velocity_and_elapsed_time(*,
                                                            start_velocity: str | None,
                                                            end_velocity: str | None,
                                                            elapsed_time: str | None,
                                                            ) -> str | None:
        
        try:
            validated_start_velocity: str = validate_value_type(value=start_velocity, value_type=(str,))
            validated_end_velocity: str = validate_value_type(value=end_velocity, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            delta_velocity: Decimal = Decimal(value=validated_end_velocity) - Decimal(value=validated_start_velocity)

            decimal_result: Decimal = delta_velocity / Decimal(value=validated_elapsed_time)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_delta_velocity_and_elapsed_time(*,
                                           delta_velocity: str | None,
                                           elapsed_time: str | None,
                                           ) -> str | None:
        
        try:
            validated_delta_velocity: str = validate_value_type(value=delta_velocity, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_delta_velocity) / Decimal(value=validated_elapsed_time)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_start_velocity_and_end_velocity_and_elapsed_distance(*,
                                                                start_velocity: str | None,
                                                                end_velocity: str | None,
                                                                elapsed_distance: str | None,
                                                                ) -> str | None:
        
        try:
            validated_start_velocity: str = validate_value_type(value=start_velocity, value_type=(str,))
            validated_end_velocity: str = validate_value_type(value=end_velocity, value_type=(str,))
            validated_elapsed_distance: str = validate_value_type(value=elapsed_distance, value_type=(str,))

            decimal_result: Decimal = (Decimal(value=validated_end_velocity) ** 2 - Decimal(value=validated_start_velocity) ** 2) / (2 * Decimal(value=validated_elapsed_distance))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_total_force_and_mass(*,
                                total_force: str | None,
                                mass: str | None,
                                ) -> str | None:
        
        try:
            validated_total_force: str = validate_value_type(value=total_force, value_type=(str,))
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_total_force) / Decimal(value=validated_mass)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    solution_by_start_velocity_and_end_velocity_and_elapsed_time: str | None = by_start_velocity_and_end_velocity_and_elapsed_time(start_velocity=start_velocity,
                                                                                                                                   end_velocity=end_velocity,
                                                                                                                                   elapsed_time=elapsed_time,
                                                                                                                                   )
    
    solution_by_delta_velocity_and_elapsed_time: str | None = by_delta_velocity_and_elapsed_time(delta_velocity=delta_velocity,
                                                                                                 elapsed_time=elapsed_time,
                                                                                                 )
    
    solution_by_start_velocity_and_end_velocity_and_elapsed_distance: str | None = by_start_velocity_and_end_velocity_and_elapsed_distance(start_velocity=start_velocity,
                                                                                                                                           end_velocity=end_velocity,
                                                                                                                                           elapsed_distance=elapsed_distance,
                                                                                                                                           )
    
    solution_by_total_force_and_mass: str | None = by_total_force_and_mass(total_force=total_force,
                                                                           mass=mass
                                                                           )
    
    solution_list: list[str | None] = [
        solution_by_start_velocity_and_end_velocity_and_elapsed_time,
        solution_by_delta_velocity_and_elapsed_time,
        solution_by_start_velocity_and_end_velocity_and_elapsed_distance,
        solution_by_total_force_and_mass,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_start_velocity(*,
                       delta_velocity: str | None = None,
                       end_velocity: str | None = None,
                       acceleration: str | None = None,
                       elapsed_distance: str | None = None,
                       elapsed_time: str | None = None,
                       average_velocity: str | None = None,
                       ) -> str | None:
    
    def by_delta_velocity_and_end_velocity(*,
                                        delta_velocity: str | None,
                                        end_velocity: str | None,
                                        ) -> str | None:
        
        try:
            validated_delta_velocity: str = validate_value_type(value=delta_velocity, value_type=(str,))
            validated_end_velocity: str = validate_value_type(value=end_velocity, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_end_velocity) - Decimal(value=validated_delta_velocity)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
    
    def by_acceleration_elapsed_distance_and_elapsed_time(*,
                                                              acceleration: str | None,
                                                              elapsed_distance: str | None,
                                                              elapsed_time: str | None,
                                                              ) -> str | None:
        
        try:
            validated_acceleration: str = validate_value_type(value=acceleration, value_type=(str,))
            validated_elapsed_distance: str = validate_value_type(value=elapsed_distance, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_elapsed_distance) / Decimal(value=validated_elapsed_time) - Decimal(value=validated_acceleration) * Decimal(value=validated_elapsed_time) / 2
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_end_velocity_and_acceleration_and_elapsed_distance(*,
                                                              end_velocity: str | None,
                                                              acceleration: str | None,
                                                              elapsed_distance: str | None,
                                                              ) -> str | None:
        
        try:
            validated_end_velocity: str = validate_value_type(value=end_velocity, value_type=(str,))
            validated_acceleration: str = validate_value_type(value=acceleration, value_type=(str,))
            validated_elapsed_distance: str = validate_value_type(value=elapsed_distance, value_type=(str,))

            decimal_result: Decimal = Decimal(Decimal(value=validated_end_velocity) ** 2 - 2 * Decimal(value=validated_acceleration) * Decimal(value=validated_elapsed_distance)).sqrt()
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_average_velocity_and_acceleration_and_elapsed_time(*,
                                                              average_velocity: str | None,
                                                              acceleration: str | None,
                                                              elapsed_time: str | None,
                                                              ) -> str | None:
        
        try:
            validated_average_velocity: str = validate_value_type(value=average_velocity, value_type=(str,))
            validated_acceleration: str = validate_value_type(value=acceleration, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            decimal_result: Decimal = 2 * Decimal(value=validated_average_velocity) - Decimal(value=validated_acceleration) * Decimal(value=validated_elapsed_time) / 2
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    solution_by_delta_velocity_and_end_velocity: str | None = by_delta_velocity_and_end_velocity(delta_velocity=delta_velocity,
                                                                                           end_velocity=end_velocity,
                                                                                           )

    solution_by_acceleration_elapsed_distance_and_elapsed_time: str | None = by_acceleration_elapsed_distance_and_elapsed_time(acceleration=acceleration,
                                                                                                                                       elapsed_distance=elapsed_distance,
                                                                                                                                       elapsed_time=elapsed_time
                                                                                                                                       )

    solution_by_end_velocity_and_acceleration_and_elapsed_distance: str | None = by_end_velocity_and_acceleration_and_elapsed_distance(end_velocity=end_velocity,
                                                                                                                                       acceleration=acceleration,
                                                                                                                                       elapsed_distance=elapsed_distance,
                                                                                                                                       )

    solution_by_average_velocity_and_acceleration_and_elapsed_time: str | None = by_average_velocity_and_acceleration_and_elapsed_time(average_velocity=average_velocity,
                                                                                                                                       acceleration=acceleration,
                                                                                                                                       elapsed_time=elapsed_time,
                                                                                                                                       )

    solution_list: list[str | None] = [
        solution_by_delta_velocity_and_end_velocity,
        solution_by_acceleration_elapsed_distance_and_elapsed_time,
        solution_by_end_velocity_and_acceleration_and_elapsed_distance,
        solution_by_average_velocity_and_acceleration_and_elapsed_time,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_average_velocity(*,
                         start_velocity: str | None = None,
                         end_velocity: str | None = None,
                         delta_velocity: str | None = None,
                         acceleration: str | None = None,
                         elapsed_time: str | None = None,
                         ) -> str | None:
    
    def by_start_velocity_and_end_velocity(*,
                                           start_velocity: str | None,
                                           end_velocity: str | None,
                                           ) -> str | None:
        
        try:
            validated_start_velocity: str = validate_value_type(value=start_velocity, value_type=(str,))
            validated_end_velocity: str = validate_value_type(value=end_velocity, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_end_velocity) + Decimal(value=validated_start_velocity) / 2
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_start_velocity_and_delta_velocity(*,
                                             start_velocity: str | None,
                                             delta_velocity: str | None,
                                             ) -> str | None:
        
        try:
            validated_start_velocity: str = validate_value_type(value=start_velocity, value_type=(str,))
            validated_delta_velocity: str = validate_value_type(value=delta_velocity, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_start_velocity) + Decimal(value=validated_delta_velocity) / 2
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_start_velocity_and_acceleration_and_elapsed_time(*,
                                                    start_velocity: str | None,
                                                    acceleration: str | None,
                                                    elapsed_time: str | None,
                                                    ) -> str | None:

        try:
            validated_start_velocity: str = validate_value_type(value=start_velocity, value_type=(str,))
            validated_acceleration: str = validate_value_type(value=acceleration, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_start_velocity) + Decimal(value=validated_acceleration) * Decimal(value=validated_elapsed_time) / 2
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
          
    solution_by_start_velocity_and_end_velocity: str | None = by_start_velocity_and_end_velocity(start_velocity=start_velocity,
                                                                                                 end_velocity=end_velocity,
                                                                                                 )
    
    solution_by_start_velocity_and_delta_velocity: str | None = by_start_velocity_and_delta_velocity(start_velocity=start_velocity,
                                                                                                     delta_velocity=delta_velocity,
                                                                                                     )

    solution_by_start_velocity_and_acceleration_and_elapsed_time: str | None = by_start_velocity_and_acceleration_and_elapsed_time(start_velocity=start_velocity,
                                                                                                                acceleration=acceleration,
                                                                                                                elapsed_time=elapsed_time,
                                                                                                                )

    solution_list: list[str | None] = [
        solution_by_start_velocity_and_end_velocity,
        solution_by_start_velocity_and_delta_velocity,
        solution_by_start_velocity_and_acceleration_and_elapsed_time,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_end_velocity(*,
                     delta_velocity: str | None = None,
                     start_velocity: str | None = None,
                     acceleration: str | None = None,
                     elapsed_distance: str | None = None,
                     elapsed_time: str | None = None,
                     average_velocity: str | None = None,
                     ) -> str | None:
    
    def by_delta_velocity_and_start_velocity(*,
                                             delta_velocity: str | None,
                                             start_velocity: str | None,
                                             ) -> str | None:
        
        try:
            validated_delta_velocity: str = validate_value_type(value=delta_velocity, value_type=(str,))
            validated_start_velocity: str = validate_value_type(value=start_velocity, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_start_velocity) + Decimal(value=validated_delta_velocity)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_start_velocity_and_acceleration_and_elapsed_time(*,
                                                            start_velocity: str | None,
                                                            acceleration: str | None,
                                                            elapsed_time: str | None,
                                                            ) -> str | None:
        
        try:
            validated_start_velocity: str = validate_value_type(value=start_velocity, value_type=(str,))
            validated_acceleration: str = validate_value_type(value=acceleration, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_start_velocity) + Decimal(value=validated_acceleration) * Decimal(value=validated_elapsed_time)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_start_velocity_and_acceleration_and_elapsed_distance(*,
                                                                start_velocity: str | None,
                                                                acceleration: str | None,
                                                                elapsed_distance: str | None,
                                                                ) -> str | None:
        
        try:
            validated_start_velocity: str = validate_value_type(value=start_velocity, value_type=(str,))
            validated_acceleration: str = validate_value_type(value=acceleration, value_type=(str,))
            validated_elapsed_distance: str = validate_value_type(value=elapsed_distance, value_type=(str,))

            decimal_result: Decimal = Decimal(Decimal(value=validated_start_velocity) ** 2 + 2 * Decimal(value=validated_acceleration) * Decimal(value=validated_elapsed_distance)).sqrt()
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
    
    def by_elapsed_distance_and_elapsed_time_and_start_velocity(*,
                                                                elapsed_distance: str | None,
                                                                elapsed_time: str | None,
                                                                start_velocity: str | None,
                                                                ) -> str | None:
        
        try:
            validated_elapsed_distance: str = validate_value_type(value=elapsed_distance, value_type=(str,))
            validated_elapsed_time: str = validate_value_type(value=elapsed_time, value_type=(str,))
            validated_start_velocity: str = validate_value_type(value=start_velocity, value_type=(str,))

            decimal_result: Decimal = 2 * Decimal(value=validated_elapsed_distance) / Decimal(value=validated_elapsed_time) - Decimal(value=validated_start_velocity)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_average_velocity_and_start_velocity(*,
                                               average_velocity: str | None,
                                               start_velocity: str | None,
                                               ) -> str | None:
        
        try:
            validated_average_velocity: str = validate_value_type(value=average_velocity, value_type=(str,))
            validated_start_velocity: str = validate_value_type(value=start_velocity, value_type=(str,))

            decimal_result: Decimal = 2 * Decimal(value=validated_average_velocity) - Decimal(value=validated_start_velocity)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    solution_by_delta_velocity_and_start_velocity: str | None = by_delta_velocity_and_start_velocity(delta_velocity=delta_velocity,
                                                                                                     start_velocity=start_velocity,
                                                                                                     )

    solution_by_start_velocity_and_acceleration_and_elapsed_time: str | None = by_start_velocity_and_acceleration_and_elapsed_time(start_velocity=start_velocity,
                                                                                                                                   acceleration=acceleration,
                                                                                                                                   elapsed_time=elapsed_time,
                                                                                                                                   )

    solution_by_start_velocity_and_acceleration_and_elapsed_distance: str | None = by_start_velocity_and_acceleration_and_elapsed_distance(start_velocity=start_velocity,
                                                                                                                                           acceleration=acceleration,
                                                                                                                                           elapsed_distance=elapsed_distance,
                                                                                                                                           )

    solution_by_elapsed_distance_and_elapsed_time_and_start_velocity: str | None = by_elapsed_distance_and_elapsed_time_and_start_velocity(elapsed_distance=elapsed_distance,
                                                                                                                                           elapsed_time=elapsed_time,
                                                                                                                                           start_velocity=start_velocity,
                                                                                                                                           )

    solution_by_average_velocity_and_start_velocity: str | None = by_average_velocity_and_start_velocity(average_velocity=average_velocity,
                                                                                                         start_velocity=start_velocity,
                                                                                                         )

    solution_list: list[str | None] = [
        solution_by_delta_velocity_and_start_velocity,
        solution_by_start_velocity_and_acceleration_and_elapsed_time,
        solution_by_start_velocity_and_acceleration_and_elapsed_distance,
        solution_by_elapsed_distance_and_elapsed_time_and_start_velocity,
        solution_by_average_velocity_and_start_velocity,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result
            
#Formulas of Static

def get_density(*,
                mass: str | None = None,
                volume: str | None = None,
                total_force: str | None = None,
                acceleration: str | None = None,
                sensible_heat: str | None = None,
                specific_heat: str | None = None,
                delta_temperature: str | None = None,
                start_temperature: str | None = None,
                end_temperature: str | None = None,
                kinetic_energy: str | None = None,
                velocity: str | None = None,
                potential_energy: str | None = None,
                gravity_acceleration: str | None = None,
                height: str | None = None,
                fusion_heat: str | None = None,
                specific_fusion_heat: str | None = None,
                mole: str | None = None,
                molar_mass: str | None = None,
                ) -> str | None:
    
    def by_mass_and_volume(*,
                           mass: str | None,
                           volume: str | None,
                           ) -> str | None:
        
        try:
            validated_mass: int | float = validate_value_type(value=mass, value_type=(str,))
            validated_volume: int | float = validate_value_type(value=volume, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_mass) / Decimal(value=validated_volume)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_total_force_and_aceleration_and_volume(*,
                                                        total_force: str | None,
                                                        acceleration: str | None,
                                                        volume: str | None,
                                                        ) -> str | None:
        
        try:
            validated_total_force: str = validate_value_type(value=total_force, value_type=(str,))
            validated_acceleration: str = validate_value_type(value=acceleration, value_type=(str,))
            validated_volume: str = validate_value_type(value=volume, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_total_force) / (Decimal(value=validated_acceleration) * Decimal(value=validated_volume))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_sensible_heat_and_specific_heat_and_delta_temperature_and_volume(*,
                                                                                     sensible_heat: str | None,
                                                                                     specific_heat: str | None,
                                                                                     delta_temperature: str | None,
                                                                                     volume: str | None,
                                                                                     ) -> str | None:
        
        try:
            validated_sensible_heat: str = validate_value_type(value=sensible_heat, value_type=(str,))
            validated_specific_heat: str = validate_value_type(value=specific_heat, value_type=(str,))
            validated_delta_temperature: str = validate_value_type(value=delta_temperature, value_type=(str,))
            validated_volume: str = validate_value_type(value=volume, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_sensible_heat) / (Decimal(value=validated_specific_heat) * Decimal(value=validated_delta_temperature) * Decimal(value=validated_volume))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_sensible_heat_and_specific_heat_and_start_temperature_and_end_temperature_and_volume(*,
                                                                                                         sensible_heat: str | None,
                                                                                                         specific_heat: str | None,
                                                                                                         start_temperature: str | None,
                                                                                                         end_temperature: str | None,
                                                                                                         volume: str | None,
                                                                                                         ) -> str | None:
        
        try:
            validated_sensible_heat: str = validate_value_type(value=sensible_heat, value_type=(str,))
            validated_specific_heat: str = validate_value_type(value=specific_heat, value_type=(str,))
            validated_start_temperature: str = validate_value_type(value=start_temperature, value_type=(str,))
            validated_end_temperature: str = validate_value_type(value=end_temperature, value_type=(str,))
            validated_volume: str = validate_value_type(value=volume, value_type=(str,))

            validated_delta_temperature: Decimal = Decimal(value=validated_end_temperature) - Decimal(value=validated_start_temperature)

            decimal_result: Decimal = Decimal(value=validated_sensible_heat) / (Decimal(value=validated_specific_heat) * validated_delta_temperature * Decimal(value=validated_volume))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_kinetic_energy_and_velocity_and_volume(*,
                                       kinetic_energy: str | None,
                                       velocity: str | None,
                                       volume: str | None,
                                       ) -> str | None:
        
        try:
            validated_kinetic_energy: str = validate_value_type(value=kinetic_energy, value_type=(str,))
            validated_velocity: str = validate_value_type(value=velocity, value_type=(str,))
            validated_volume: str  = validate_value_type(value=volume, value_type=(str,))

            decimal_result: Decimal = (Decimal(value=validated_kinetic_energy) * 2) / (Decimal(value=validated_velocity) ** 2 * Decimal(value=validated_volume))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_potential_energy_and_gravity_acceleration_and_height_and_volume(*,
                                                                           potential_energy: str | None,
                                                                           gravity_acceleration: str | None,
                                                                           height: str | None,
                                                                           volume: str | None,
                                                                           ) -> str | None:
        
        try:
            validated_potential_energy: str = validate_value_type(value=potential_energy, value_type=(str,))
            validated_gravity_acceleration: str = validate_value_type(value=gravity_acceleration, value_type=(str,))
            validated_height: str = validate_value_type(value=height, value_type=(str,))
            validated_volume: str = validate_value_type(value=volume, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_potential_energy) / (Decimal(value=validated_gravity_acceleration) * Decimal(value=validated_height) * Decimal(value=validated_volume))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_fusion_heat_and_specific_fusion_heat_and_volume(*,
                                                           fusion_heat: str | None,
                                                           specific_fusion_heat: str | None,
                                                           volume: str | None,
                                                           ) -> str | None:
        
        try:
            validated_fusion_heat: str = validate_value_type(value=fusion_heat, value_type=(str,))
            validated_specific_fusion_heat: str = validate_value_type(value=specific_fusion_heat, value_type=(str,))
            validated_volume: str = validate_value_type(value=volume, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_fusion_heat) / (Decimal(value=validated_specific_fusion_heat) * Decimal(value=validated_volume))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
                
    def by_mole_and_molar_mass_and_volume(*,
                                          mole: str | None,
                                          molar_mass: str | None,
                                          volume: str | None,
                                          ) -> str | None:
        
        try:
            validated_mole: str = validate_value_type(value=mole, value_type=(str,))
            validated_molar_mass: str = validate_value_type(value=molar_mass, value_type=(str,))
            validated_volume: str = validate_value_type(value=volume, value_type=(str,))

            decimal_result: Decimal = (Decimal(value=validated_mole) * Decimal(value=validated_molar_mass)) / Decimal(value=validated_volume)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    solution_by_mass_and_volume: str | None = by_mass_and_volume(mass=mass, 
                                                                   volume=volume
                                                                   )
    
    solution_by_total_force_and_aceleration_and_volume: str | None = by_total_force_and_aceleration_and_volume(total_force=total_force, 
                                                                                                                             acceleration=acceleration,
                                                                                                                             volume=volume,
                                                                                                                             )

    solution_by_sensible_heat_and_specific_heat_and_delta_temperature_and_volume: str | None = by_sensible_heat_and_specific_heat_and_delta_temperature_and_volume(sensible_heat=sensible_heat,
                                                                                                                                                                                       specific_heat=specific_heat,
                                                                                                                                                                                       delta_temperature=delta_temperature,
                                                                                                                                                                                       volume=volume,
                                                                                                                                                                                       )
    
    solution_by_sensible_heat_and_specific_heat_and_start_temperature_and_end_temperature_and_volume: str | None = by_sensible_heat_and_specific_heat_and_start_temperature_and_end_temperature_and_volume(sensible_heat=sensible_heat,
                                                                                                                                                                                                                               specific_heat=specific_heat,
                                                                                                                                                                                                                               start_temperature=start_temperature,
                                                                                                                                                                                                                               end_temperature=end_temperature,
                                                                                                                                                                                                                               volume=volume,
                                                                                                                                                                                                                               )
    
    solution_by_kinetic_energy_and_velocity_and_volume: str | None = by_kinetic_energy_and_velocity_and_volume(kinetic_energy=kinetic_energy,
                                                                                                                 velocity=velocity,
                                                                                                                 volume=volume,
                                                                                                                 )

    solution_by_potential_energy_and_gravity_acceleration_and_height_and_volume: str | None = by_potential_energy_and_gravity_acceleration_and_height_and_volume(potential_energy=potential_energy,
                                                                                                                                                                   gravity_acceleration=gravity_acceleration,
                                                                                                                                                                   height=height,
                                                                                                                                                                   volume=volume,
                                                                                                                                                                   )
    
    solution_by_fusion_heat_and_specific_fusion_heat_and_volume: str | None = by_fusion_heat_and_specific_fusion_heat_and_volume(fusion_heat=fusion_heat,
                                                                                                                                   specific_fusion_heat=specific_fusion_heat,
                                                                                                                                   volume=volume,
                                                                                                                                   )
    
    solution_by_mole_and_molar_mass_and_volume: str | None = by_mole_and_molar_mass_and_volume(mole=mole,
                                                                                                 molar_mass=molar_mass,
                                                                                                 volume=volume,
                                                                                                 )
    
    solution_list: list[str | None] = [
        solution_by_mass_and_volume,
        solution_by_total_force_and_aceleration_and_volume,
        solution_by_sensible_heat_and_specific_heat_and_delta_temperature_and_volume,
        solution_by_sensible_heat_and_specific_heat_and_start_temperature_and_end_temperature_and_volume,
        solution_by_kinetic_energy_and_velocity_and_volume,
        solution_by_potential_energy_and_gravity_acceleration_and_height_and_volume,
        solution_by_fusion_heat_and_specific_fusion_heat_and_volume,
        solution_by_mole_and_molar_mass_and_volume,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_volume(*,
               mass: str | None = None,
               density: str | None = None,
               total_force: str | None = None,
               acceleration: str | None = None,
               sensible_heat: str | None = None,
               specific_heat: str | None = None,
               delta_temperature: str | None = None,
               start_temperature: str | None = None,
               end_temperature: str | None = None,
               kinetic_energy: str | None = None,
               velocity: str | None = None,
               potential_energy: str | None = None,
               gravity_acceleration: str | None = None,
               height: str | None = None,
               fusion_heat: str | None = None,
               specific_fusion_heat: str | None = None,
               mole: str | None = None,
               molar_mass: str | None = None,
               ) -> str | None:
    
    def by_mass_and_density(*,
                            mass: str | None,
                            density: str | None,
                            ) -> str | None:
        
        try:
            validate_mass: str = validate_value_type(value=mass, value_type=(str,))
            validate_density: str = validate_value_type(value=density, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validate_mass) / Decimal(value=validate_density)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_total_force_and_acceleration_and_density(*,
                                                   total_force: str | None,
                                                   acceleration: str | None,
                                                   density: str | None,
                                                   ) -> str | None:
        
        try:
            validated_total_force: str = validate_value_type(value=total_force, value_type=(str,))
            validated_acceleration: str = validate_value_type(value=acceleration, value_type=(str,))
            validated_density: str = validate_value_type(value=density, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_total_force) / (Decimal(value=validated_acceleration) * Decimal(value=validated_density))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_sensible_heat_and_specific_heat_and_delta_temperature_and_density(*,
                                                                                      sensible_heat: str | None,
                                                                                      specific_heat: str | None,
                                                                                      delta_temperature: str | None,
                                                                                      density: str | None,
                                                                                      ) -> str | None:
        
        try:
            validated_sensible_heat: str = validate_value_type(value=sensible_heat, value_type=(str,))
            validated_specific_heat: str = validate_value_type(value=specific_heat, value_type=(str,))
            validated_delta_temperature: str = validate_value_type(value=delta_temperature, value_type=(str,))
            validated_density: str = validate_value_type(value=density, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_sensible_heat) / (Decimal(value=validated_specific_heat) * Decimal(value=validated_delta_temperature) * Decimal(value=validated_density))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_sensible_heat_and_specific_heat_and_start_temperature_and_end_temperature_and_density(*,
                                                                                                          sensible_heat: str | None,
                                                                                                          specific_heat: str | None,
                                                                                                          start_temperature: str | None,
                                                                                                          end_temperature: str | None,
                                                                                                          density: str | None,
                                                                                                          ) -> str | None:
        
        try:
            validated_sensible_heat: str = validate_value_type(value=sensible_heat, value_type=(str,))
            validated_specific_heat: str = validate_value_type(value=specific_heat, value_type=(str,))
            validated_start_temperature: str = validate_value_type(value=start_temperature, value_type=(str,))
            validated_end_temperature: str = validate_value_type(value=end_temperature, value_type=(str,))
            validated_density: str = validate_value_type(value=density, value_type=(str,))

            validated_delta_temperature: Decimal = Decimal(value=validated_end_temperature) - Decimal(value=validated_start_temperature)

            decimal_result: Decimal = Decimal(value=validated_sensible_heat) / (Decimal(value=validated_specific_heat) * validated_delta_temperature * Decimal(value=validated_density))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_kinetic_energy_and_velocity_and_density(*,
                                       kinetic_energy: str | None,
                                       velocity: str | None,
                                       density: str | None,
                                       ) -> str | None:
        
        try:
            validated_kinetic_energy: str = validate_value_type(value=kinetic_energy, value_type=(str,))
            validated_velocity: str = validate_value_type(value=velocity, value_type=(str,))
            validated_density: str = validate_value_type(value=density, value_type=(str,))

            decimal_result: Decimal = (Decimal(value=validated_kinetic_energy) * 2) / (Decimal(value=validated_velocity) * Decimal(value=validated_density))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_potential_energy_and_gravity_acceleration_and_height_and_density(*,
                                                                potential_energy: str | None,
                                                                gravity_acceleration: str | None,
                                                                height: str | None,
                                                                density: str | None,
                                                                ) -> str | None:
        
        try:
            validated_potential_energy: str = validate_value_type(value=potential_energy, value_type=(str,))
            validated_gravity_acceleration: str = validate_value_type(value=gravity_acceleration, value_type=(str,))
            validated_height: str = validate_value_type(value=height, value_type=(str,))
            validated_density: str = validate_value_type(value=density, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_potential_energy) / (Decimal(value=validated_gravity_acceleration) * Decimal(value=validated_height) * Decimal(value=validated_density))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_fusion_heat_and_specific_fusion_heat_and_density(*,
                                                            fusion_heat: str | None,
                                                            specific_fusion_heat: str | None,
                                                            density: str | None,
                                                            ) -> str | None:
        
        try:
            validated_fusion_heat: str = validate_value_type(value=fusion_heat, value_type=(str,))
            validated_specific_fusion_heat: str = validate_value_type(value=specific_fusion_heat, value_type=(str,))
            validated_density: str = validate_value_type(value=density, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_fusion_heat) / (Decimal(value=validated_specific_fusion_heat) * Decimal(value=validated_density))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_mole_and_and_molar_mass_and_density(*,
                                               mole: str | None,
                                               molar_mass: str | None,
                                               density: str | None,
                                               ) -> str | None:
        
        try:
            validated_mole: str = validate_value_type(value=mole, value_type=(str,))
            validated_molar_mass: str = validate_value_type(value=molar_mass, value_type=(str,))
            validated_density: str = validate_value_type(value=density, value_type=(str,))

            decimal_result: Decimal = (Decimal(value=validated_mole) * Decimal(value=validated_molar_mass)) / Decimal(value=validated_density)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
               
    solution_by_mass_and_density: str | None = by_mass_and_density(mass=mass,
                                                                     density=density
                                                                     )

    solution_by_total_force_and_aceleration_and_density: str | None = by_total_force_and_acceleration_and_density(total_force=total_force,
                                                                                                                    acceleration=acceleration,
                                                                                                                    density=density,
                                                                                                                    )
    
    solution_by_sensible_heat_and_specific_heat_and_delta_temperature_and_density: str | None = by_sensible_heat_and_specific_heat_and_delta_temperature_and_density(sensible_heat=sensible_heat,
                                                                                                                                                                                         specific_heat=specific_heat,
                                                                                                                                                                                         delta_temperature=delta_temperature,
                                                                                                                                                                                         density=density,
                                                                                                                                                                                         )
    
    solution_by_sensible_heat_and_specific_heat_and_start_temperature_and_end_temperature_and_density: str | None = by_sensible_heat_and_specific_heat_and_start_temperature_and_end_temperature_and_density(sensible_heat=sensible_heat,
                                                                                                                                                                                                                                 specific_heat=specific_heat,
                                                                                                                                                                                                                                 start_temperature=start_temperature,
                                                                                                                                                                                                                                 end_temperature=end_temperature,
                                                                                                                                                                                                                                 density=density,
                                                                                                                                                                                                                                 )
    
    solution_by_fusion_heat_and_specific_fusion_heat_and_density: str | None = by_fusion_heat_and_specific_fusion_heat_and_density(fusion_heat=fusion_heat,
                                                                                                                                     specific_fusion_heat=specific_fusion_heat,
                                                                                                                                     density=density,
                                                                                                                                     )
    
    solution_by_kinetic_energy_and_velocity_and_density: str | None = by_kinetic_energy_and_velocity_and_density(kinetic_energy=kinetic_energy,
                                                                                           velocity=velocity,
                                                                                           density=density,
                                                                                           )
    
    solution_by_potential_energy_and_gravity_acceleration_and_height_and_density: str | None = by_potential_energy_and_gravity_acceleration_and_height_and_density(potential_energy=potential_energy,
                                                                                                                                             gravity_acceleration=gravity_acceleration,
                                                                                                                                             height=height,
                                                                                                                                             density=density,
                                                                                                                                             )
    
    solution_by_mole_and_and_molar_mass_and_density: str | None = by_mole_and_and_molar_mass_and_density(mole=mole,
                                                                                                           molar_mass=molar_mass,
                                                                                                           density=density,
                                                                                                           )
    
    solution_list: list[str | None] = [
        solution_by_mass_and_density,
        solution_by_total_force_and_aceleration_and_density,
        solution_by_sensible_heat_and_specific_heat_and_delta_temperature_and_density,
        solution_by_sensible_heat_and_specific_heat_and_start_temperature_and_end_temperature_and_density,
        solution_by_fusion_heat_and_specific_fusion_heat_and_density,
        solution_by_kinetic_energy_and_velocity_and_density,
        solution_by_potential_energy_and_gravity_acceleration_and_height_and_density,
        solution_by_mole_and_and_molar_mass_and_density,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_mass(*,
             density: str | None = None,
             volume: str | None = None,
             total_force: str | None = None,
             acceleration: str | None = None,
             sensible_heat: str | None = None,
             specific_heat: str | None = None,
             delta_temperature: str | None = None,
             start_temperature: str | None = None,
             end_temperature: str | None = None,
             kinetic_energy: str | None = None,
             velocity: str | None = None,
             potential_energy: str | None = None,
             gravity_acceleration: str | None = None,
             height: str | None = None,
             fusion_heat: str | None = None,
             specific_fusion_heat: str | None = None,
             mole: str | None = None,
             molar_mass: str | None = None,
             ) -> str | None:
    
    def by_density_and_volume(*,
                              density: str | None,
                              volume: str | None,
                              ) -> str | None:
        
        try:
            validated_density: str = validate_value_type(value=density, value_type=(str,))
            validated_volume: str = validate_value_type(value=volume, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_density) * Decimal(value=validated_volume)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_total_force_and_acceleration(*,
                                        total_force: str | None,
                                        acceleration: str | None,
                                        ) -> str | None:
        
        try:
            validated_total_force: str = validate_value_type(value=total_force, value_type=(str,))
            validated_acceleration: str = validate_value_type(value=acceleration, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_total_force) / Decimal(value=validated_acceleration)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_sensible_heat_and_specific_heat_and_delta_temperature(*,
                                                                          sensible_heat: str | None,
                                                                          specific_heat: str | None,
                                                                          delta_temperature: str | None
                                                                          ) -> str | None:
        
        try:
            validated_sensible_heat: str = validate_value_type(value=sensible_heat, value_type=(str,))
            validated_specific_heat: str = validate_value_type(value=specific_heat, value_type=(str,))
            validated_delta_temperature: str = validate_value_type(value=delta_temperature, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_sensible_heat) / (Decimal(value=validated_specific_heat) * Decimal(value=validated_delta_temperature))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_sensible_heat_and_specific_heat_and_start_temperature_and_end_temperature(*,
                                                                                              sensible_heat: str | None,
                                                                                              specific_heat: str | None,
                                                                                              start_temperature: str | None,
                                                                                              end_temperature: str | None,
                                                                                              ) -> str | None:
        
        try:
            validated_sensible_heat: str = validate_value_type(value=sensible_heat, value_type=(str,))
            validated_specific_heat: str = validate_value_type(value=specific_heat, value_type=(str,))
            validated_start_temperature: str = validate_value_type(value=start_temperature, value_type=())
            validated_end_temperature: str = validate_value_type(value=end_temperature, value_type=(str,))

            validated_delta_temperature: Decimal = Decimal(value=validated_end_temperature) - Decimal(value=validated_start_temperature)

            decimal_result: Decimal = Decimal(value=validated_sensible_heat) / (Decimal(value=validated_specific_heat) * validated_delta_temperature)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_kinetic_energy_and_velocity(*,
                                       kinetic_energy: str | None,
                                       velocity: str | None,
                                       ) -> str | None:
        
        try:
            validated_kinetic_energy: str = validate_value_type(value=kinetic_energy, value_type=(str,))
            validated_velocity: str = validate_value_type(value=velocity, value_type=(str,))

            decimal_result: Decimal = (Decimal(value=validated_kinetic_energy) * 2) / (Decimal(value=validated_velocity) ** 2)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_potential_energy_and_gravity_acceleration_and_height(*,
                                                                potential_energy: str | None,
                                                                gravity_acceleration: str | None,
                                                                height: str | None,
                                                                ) -> str | None:
        
        try:
            validated_potential_energy: str = validate_value_type(value=potential_energy, value_type=(str,))
            validated_gravity_acceleration: str = validate_value_type(value=gravity_acceleration, value_type=(str,))
            validated_height: str = validate_value_type(value=height, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_potential_energy) / (Decimal(value=validated_gravity_acceleration) * Decimal(value=validated_height))
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_fusion_heat_and_specific_fusion_heat(*,
                                                fusion_heat: str | None,
                                                specific_fusion_heat: str | None
                                                ) -> str | None:
        
        try:
            validated_fusion_heat: str = validate_value_type(value=fusion_heat, value_type=(str,))
            validated_specific_fusion_heat: str = validate_value_type(value=specific_fusion_heat, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_fusion_heat) / Decimal(value=validated_specific_fusion_heat)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
        
    def by_mole_and_molar_mass(*,
                               mole: str | None,
                               molar_mass: str | None,
                               ) -> str | None:
        
        try:
            validated_mole: str = validate_value_type(value=mole, value_type=(str,))
            validated_molar_mass: str = validate_value_type(value=molar_mass, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_mole) * Decimal(value=validated_molar_mass)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    solution_by_density_and_volume: str | None = by_density_and_volume(density=density, 
                                                                               volume=volume,
                                                                               )
    
    solution_by_total_force_and_acceleration: str | None = by_total_force_and_acceleration(total_force=total_force,
                                                                                             acceleration=acceleration,
                                                                                             )
    
    solution_by_sensible_heat_and_specific_heat_and_delta_temperature: str | None = by_sensible_heat_and_specific_heat_and_delta_temperature(sensible_heat=sensible_heat,
                                                                                                                                                                 specific_heat=specific_heat,
                                                                                                                                                                 delta_temperature=delta_temperature,
                                                                                                                                                                 )
    
    solution_by_sensible_heat_and_specific_heat_and_start_temperature_and_end_temperature: str | None = by_sensible_heat_and_specific_heat_and_start_temperature_and_end_temperature(sensible_heat=sensible_heat,
                                                                                                                                                                                                         specific_heat=specific_heat,
                                                                                                                                                                                                         start_temperature=start_temperature,
                                                                                                                                                                                                         end_temperature=end_temperature,
                                                                                                                                                                                                         )
    
    solution_by_kinetic_energy_and_velocity: str | None = by_kinetic_energy_and_velocity(kinetic_energy=kinetic_energy,
                                                                                           velocity=velocity,
                                                                                           )
    
    solution_by_potential_energy_and_gravity_acceleration_and_height: str | None = by_potential_energy_and_gravity_acceleration_and_height(potential_energy=potential_energy,
                                                                                                                                             gravity_acceleration=gravity_acceleration,
                                                                                                                                             height=height,
                                                                                                                                             )
    
    solution_by_fusion_heat_and_specific_fusion_heat: str | None = by_fusion_heat_and_specific_fusion_heat(fusion_heat=fusion_heat,
                                                                                                             specific_fusion_heat=specific_fusion_heat,
                                                                                                             )
    
    solution_by_mole_and_molar_mass: str | None = by_mole_and_molar_mass(mole=mole,
                                                                                 molar_mass=molar_mass,
                                                                                 )
    
    solution_list: list[str | None] = [
        solution_by_density_and_volume,
        solution_by_total_force_and_acceleration,
        solution_by_sensible_heat_and_specific_heat_and_delta_temperature,
        solution_by_kinetic_energy_and_velocity,
        solution_by_potential_energy_and_gravity_acceleration_and_height,
        solution_by_sensible_heat_and_specific_heat_and_start_temperature_and_end_temperature,
        solution_by_fusion_heat_and_specific_fusion_heat,
        solution_by_mole_and_molar_mass,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_force_pressure(*,
                 force: str | None = None,
                 area: str | None = None,
                 ) -> str | None:
    
    def by_force_and_area(*,
                          force: str | None,
                          area: str | None,
                          ) -> str | None:
    
        try:
            validated_force: str = validate_value_type(value=force, value_type=(str,))
            validated_area: str = validate_value_type(value=area, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_force) / Decimal(value=validated_area)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except (TypeError, ZeroDivisionError):
            return None
    
    solution_by_force_and_area: str | None = by_force_and_area(force=force,
                                                               area=area,
                                                               )
    
    solution_list: list[str | None] = [
        solution_by_force_and_area,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result
    
def get_hydrostatic_pressure(*,
                             density: str | None = None,
                             gravity_acceleration: str | None = None,
                             height: str | None = None,
                             ) -> str | None:
    
    def by_density_and_gravity_acceleration_and_height(*,
                                                       density: str | None,
                                                       gravity_acceleration: str | None,
                                                       height: str | None,
                                                       ) -> str | None:
    
        try:
            validated_density: str = validate_value_type(value=density, value_type=(str,))
            validated_gravity_acceleration: str = validate_value_type(value=gravity_acceleration, value_type=(str,))
            validated_height: str = validate_value_type(value=height, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_density) * Decimal(value=validated_gravity_acceleration) * Decimal(value=validated_height)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    solution_by_density_and_gravity_acceleration_and_height: str | None = by_density_and_gravity_acceleration_and_height(density=density,
                                                                                                                         gravity_acceleration=gravity_acceleration,
                                                                                                                         height=height,
                                                                                                                         )
    
    solution_list: list[str | None] = [
        solution_by_density_and_gravity_acceleration_and_height,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

def get_archimedes_force(*,
                         density: str | None = None,
                         gravity_acceleration: str | None = None,
                         volume: str | None = None,
                         mass: str | None = None,
                         ) -> str | None:
    
    def by_density_and_gravity_acceleration_and_volume(*,
                                                       density: str | None,
                                                       gravity_acceleration: str | None,
                                                       volume: str | None,
                                                       ) -> str | None:
    
        try:
            validated_density: str = validate_value_type(value=density, value_type=(str,))
            validated_gravity_acceleration: str= validate_value_type(value=gravity_acceleration, value_type=(str,))
            validated_volume: str = validate_value_type(value=volume, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_density) * Decimal(value=validated_gravity_acceleration) * Decimal(value=validated_volume)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    def by_mass_and_gravity_acceleration(*,
                                         mass: str | None,
                                         gravity_acceleration: str | None,
                                         ) -> str | None:
        
        try:
            validated_mass: str = validate_value_type(value=mass, value_type=(str,))
            validated_gravity_acceleration: str = validate_value_type(value=gravity_acceleration, value_type=(str,))

            decimal_result: Decimal = Decimal(value=validated_mass) * Decimal(value=validated_gravity_acceleration)
            final_result: str = trim_trailing_zeros(decimal_number=decimal_result)
            return final_result
        except TypeError:
            return None
        
    solution_by_density_and_gravity_acceleration_and_volume: str | None = by_density_and_gravity_acceleration_and_volume(density=density,
                                                                                                                         gravity_acceleration=gravity_acceleration,
                                                                                                                         volume=volume,
                                                                                                                         )
    
    solution_by_mass_and_gravity_acceleration: str | None = by_mass_and_gravity_acceleration(mass=mass,
                                                                                             gravity_acceleration=gravity_acceleration,
                                                                                             )

    solution_list: list[str | None] = [
        solution_by_density_and_gravity_acceleration_and_volume,
        solution_by_mass_and_gravity_acceleration,
    ]

    result: str | None = get_first_value_with_given_type_from_iterator(iterator_object=solution_list, value_type=(str,))
    return result

#Approved
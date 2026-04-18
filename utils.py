from typing import Any
from decimal import Decimal
    
def get_first_value_with_given_type_from_iterator(*, iterator_object: Any, value_type: tuple[type, ...]) -> Any:
    """
    This function returns the first object of value_type in iterators. Function now works only for lists and tuples. For example

    get_first_value_with_given_type_from_iterator(iterator_object=[1, 2.0, "my_string", "4", True,], value_type=(bool, str)) returns my_string

    get_first_value_with_given_type_from_iterator(iterator_object=["14", False, [], "5678"], value_type=(int, float)) returns None
    """

    iterator_object_is_not_iterator: bool = not isinstance(iterator_object, (str, list, tuple, dict, set))
    iterator_object_is_empty: bool = not iterator_object
    iterator_object_is_not_valid: bool = iterator_object_is_not_iterator or iterator_object_is_empty

    if iterator_object_is_not_valid:
        return None
    
    result: Any = None
    
    for element in iterator_object:
        element_type_is_in_value_type: bool = isinstance(element, value_type) and not isinstance(element, bool)
        if element_type_is_in_value_type:
            result: Any = element
            break

    return result

def validate_value_type(*, value: Any, value_type: tuple[type, ...]) -> Any:
    """
    If value type is in value_type, function returns this value, else raises TypeError. For example

    validate_value_type(value=5, value_type=(int, float)) returns 5

    validate_value_type(value=5, value_type(str, bool)) raises TypeError
    """

    value_type_in_value_type_tuple: bool = isinstance(value, value_type)

    if value_type_in_value_type_tuple:
        return value
    else:
        raise TypeError

def trim_trailing_zeros(*, decimal_number: Decimal, mode: str = "f"):
    """
    This function gets number of type Decimal and returns this number without trailing zeros. For example

    trim_trailing_zeros(decimal_number=Decimal("3.141592653589790000")) returns 3.14159265358979 (That one mathematician is happy to see Pi number :) )
    """
    result: str = format(decimal_number.normalize(), mode)
    return result
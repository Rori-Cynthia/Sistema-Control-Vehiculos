from enum import StrEnum
from typing import Type, Any


class BicycleType(StrEnum):
    URBAN = "Urbana"
    RACING = "Carrera"
    SPORT = "Deportiva"


class FrameType(StrEnum):
    DOUBLE_CRADLE_FRAME = "Doble Cuna"
    MULTI_TUBULAR_FRAME = "Multitubular"
    DOUBLE_BEAM_FRAME = "Doble Viga"


class EngineType(StrEnum):
    TWO_TIMES = "2T"
    FOUR_TIMES = "4T"

def validate_enum(value: str, enumType: Type[StrEnum], parameter_description: str) -> Any:
    possible_values = [element.value for element in enumType]
    if value not in possible_values:
        raise ValueError(f"Valor inválido. Los valores posibles para "
                        f"{parameter_description} son: {', '.join(possible_values)}.")
    return enumType(value)
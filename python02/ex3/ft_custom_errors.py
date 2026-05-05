#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant(plant: str) -> None:
    sick_plants = ["tomato", "lettuce"]
    if plant in sick_plants:
        raise PlantError(f"The {plant} plant is wilting!")
    else:
        print(f"The {plant} plant is healthy!\n")


def check_water(water: int) -> None:
    if water < 5:
        raise WaterError("Not enough water in the tank!")
    else:
        print("Water is enough!\n")


def test_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        check_water(2)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    try:
        check_plant("tomato")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water(2)
    except GardenError as e:
        print(f"Caught GardenError: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_errors()

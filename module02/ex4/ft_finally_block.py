
class Colors:
    # ANSI color codes :)
    red = "\033[0;31m"
    green = "\033[0;32m"
    reset = "\033[0m"


class GardenError(Exception):

    def __init__(self, msg="Unknown Garden Error"):
        self.__msg = msg
        super().__init__(self.__msg)


class PlantError(GardenError):

    def __init__(self, msg="Unknown Plant Error"):
        self.__msg = msg
        super().__init__(self.__msg)


def water_plant(plant_name):
    if plant_name.capitalize() != plant_name:
        raise PlantError(f"{Colors.red}[OK] Caught PlantError: \
'{plant_name}' isn't capitalized...{Colors.reset}")
    else:
        print(f"Watering {plant_name}: {Colors.green}[OK]{Colors.reset}")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    valid_plants: list = [
        "Tomato",
        "Lettuce",
        "Carrots",
        "Cabbage",
        "Pineapple"
    ]

    invalid_plants = valid_plants.copy()
    invalid_plants[2] = "carrots"

# Valid plants
    print("""Testing valid plants...
Opening Watering System:""")
    try:
        for x in valid_plants:
            water_plant(x)
    except PlantError as error:
        print(f"Watering {x}: {error}")
        print("\nEnding tests and returning to main...")
        return
    finally:
        print("\n=== Closing Watering System ===")

# Invalid plants
    print("""Testing invalid plants...
Opening Watering System:""")
    try:
        for x in invalid_plants:
            water_plant(x)
    except PlantError as error:
        print(f"Watering {x}: {error}")
        print("\nEnding tests and returning to main...")
        return
    finally:
        print("\n=== Closing Watering System ===")


if __name__ == "__main__":
    test_watering_system()
    print(f"\n{Colors.green}Cleanup always happens, \
even with errors!{Colors.reset}")

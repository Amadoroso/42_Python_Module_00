
class GardenError(Exception):

    def __init__(self, msg="Unknown Garden Error"):
        self.__msg = msg
        super().__init__(self.__msg)


class PlantError(GardenError):

    def __init__(self, msg="Unknown Plant Error"):
        self.__msg = msg
        super().__init__(self.__msg)


class WaterError(GardenError):

    def __init__(self, msg="Unknown Water Error"):
        self.__msg = msg
        super().__init__(self.__msg)


def tests(var) -> None:

    if var == "chocolate":
        raise PlantError(f"{var} isn't a valid Plant name!")

    elif var == "oil":
        raise WaterError(f"{var} isn't a valid Water source!")


def Error_printing() -> None:

    print("\nTesting PlantError:")
    try:
        tests("chocolate")
    except PlantError as error:
        print(f"Caught Plant error: {error}")

    print("\nTesting WaterError:")
    try:
        tests("oil")
    except WaterError as error:
        print(f"Caught Water error: {error}")

    print("\nTesting GardenError Parent Class")
    try:
        tests("chocolate")
    except GardenError as error:
        print(f"Caught Garden error: {error}")

    try:
        tests("oil")
    except GardenError as error:
        print(f"Caught Garden error: {error}")


if __name__ == "__main__":
    Error_printing()
    print("\nAll good!")

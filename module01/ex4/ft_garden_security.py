
# Defining the class plant
class Plant:
    def __init__(self, name="N/A", height=1.0, age=1, growth_rate=1.0) -> None:
        self.__height = self.__validate("Height", height)
        self.__age = self.__validate("Age", age)
        self.__growth_rate = self.__validate("Growth Rate", growth_rate)
        self.name = name

    def __validate(self, param_name, value):
        if value > 0:
            return value
        else:
            print(f"""The {param_name} you entered is invalid. \
Please use a value > 0
The Object was created with {param_name} of 1\n""")
            return 1

    def show(self) -> None:
        print(f"Plant info: {self.name}: {round(self.__height, 1)}cm, \
{round(self.__age, 1)} days old with {round(self.__growth_rate, 1)} cm/day")

    def grow(self) -> None:
        self.__height += self.__growth_rate

    def age(self) -> None:
        self.__age += 1

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def set_height(self, height) -> None:
        if height < 0.0:
            print("""The Height you entered is invalid. Please use a value > 0
The Height was unchanged\n""")
        else:
            self.__height = height

    def set_age(self, age) -> None:
        if age < 0.0:
            print("""The Age you entered is invalid. Please use a value > 0
The Age was unchanged\n""")
        else:
            self.__age = age


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    Rose = Plant("Rose", 1, 1, 10)
    Rose.show()
    Rose.set_age(25.56)
    Rose.set_height(25.56)
    print("\n=== Modifying age and height with valid inputs ===")
    Rose.show()
    print("\n=== Modifying age and height with INVALID inputs ===")
    Rose.set_age(-25.56)
    Rose.set_height(-25.56)
    print("Rose age and height keep the previous values:")
    Rose.show()
    print("\n=== Initializing a new Plant with invalid age, \
height and growth_rate ===")
    Tulip = Plant("Tulip", -1, -1, -1)
    print("Values will be set to default")
    Tulip.show()


if __name__ == "__main__":
    ft_garden_security()

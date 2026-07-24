
#  Defining the class plant
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
        print(f"{self.name}: {round(self.__height, 1)}cm, \
{round(self.__age, 1)} days old growing {round(self.__growth_rate, 1)} cm/day")

    def grow(self) -> None:
        self.__height += self.__growth_rate

    def age(self) -> None:
        self.__age += 1

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_growth_rate(self):
        return self.__growth_rate

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


#  ================== FLOWERS ==================
class Flower(Plant):
    def __init__(self, name="Flower", height=1.0, age=1,
                 growth_rate=1.0, color="N/A") -> None:
        super().__init__(name, height, age, growth_rate)
        self.__color = self.__color_val(color)
        self.__bloom = False

    def __color_val(self, color):
        if color.isalpha():
            return color.capitalize()
        else:
            print("""The Color you entered is invalid. \
Please introduze a valid string""")

    def show(self) -> None:
        super().show()
        if self.__bloom:
            print(f"Color: {self.__color} | Bloom state: Bloomed :)!")
        else:
            print(f"Color: {self.__color} | Bloom state: Hasn't bloomed...")

    def bloom(self) -> None:
        self.__bloom = True


#  ================== TREES ==================
class Tree(Plant):
    def __init__(self, name="Tree", height=1.0, age=1,
                 growth_rate=1.0, trunk_diameter=1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self.__trunk_dia = self.__trunk_val(trunk_diameter)
        self.__shade = False

    def __trunk_val(self, trunk_diameter):
        if trunk_diameter > 0:
            return trunk_diameter
        else:
            print("""The Trunk diameter you entered is invalid. \
The Object was created with a Trunk diameter of 1""")

    def show(self) -> None:
        super().show()
        if self.__shade:
            print(f"Trunk diameter: {round(self.__trunk_dia, 1)} \
Currently producing shade ({round(self.__trunk_dia, 1)} cm \
by {self.get_age()} cm)!")
        else:
            print(f"Trunk diameter: {round(self.__trunk_dia, 1)} \
| Can't produce shade...")

    def produce_shade(self) -> None:
        self.__shade = True


#  ================== VEGGIES ==================
class Vegetable(Plant):
    def __init__(self, name="Veggie", height=1.0, age=1, growth_rate=1.0,
                 harvest_season="N/A", nutricional_val=1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self.__nutricional_val = self.__nut_val(nutricional_val)
        self.__harvest_season = self.__harvest_val(harvest_season)

    def __nut_val(self, nutritional_val):
        if nutritional_val >= 0:
            return nutritional_val
        else:
            print("""The nutritional value you entered is invalid. \
The Object was created with a nutritional value of 1""")

    def __harvest_val(self, harvest_season):
        if harvest_season.isalpha():
            return harvest_season.capitalize()
        else:
            print("""The Harvest season you entered is invalid. \
The Object was created without Harvest season""")

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.__harvest_season} | \
Nutricional Val.: {round(self.__nutricional_val, 1)}")

    def grow(self) -> None:
        super().grow()
        self.__nutricional_val += self.get_growth_rate()

    def age(self) -> None:
        super().age()
        self.__nutricional_val += self.get_growth_rate()


def ft_plant_types() -> None:
    Rose = Flower("Rose", 2, 2, 2, "Red")
    Oak = Tree("Oak", 10, 10, 10, 50.55)
    Carrot = Vegetable("Carrot", 1, 1, 1, "April", 0)
    print("=== Testing .show() override for the 3 types ===")
    Rose.show()
    print("\n")
    Oak.show()
    print("\n")
    Carrot.show()
    print("\n")
    print("=== Testing .bloom() for the flower ===")
    Rose.bloom()
    Rose.show()
    print("\n=== Testing .produce_shade() for the tree ===")
    Oak.produce_shade()
    Oak.show()
    print("\n=== Testing .age() and .grow() for the tree ===")
    for days in range(1, 21):
        Carrot.grow()
        Carrot.age()
    Carrot.show()


if __name__ == "__main__":
    ft_plant_types()


#  Defining the class plant
class Plant:
    def __init__(self, name="N/A", height=1.0, age=1, growth_rate=1.0) -> None:
        self.__height = self.__validate("Height", height)
        self.__age = self.__validate("Age", age)
        self.__growth_rate = self.__validate("Growth Rate", growth_rate)
        self.name = name
        self._Stats = self.Stats()

    @classmethod  # alternative to init, creates anon plant
    def create_anon(cls):
        return cls("Unknown Plant", 0.0, 0, 0.0)

    def __validate(self, param_name, value):
        if value >= 0:
            return value
        else:
            print(f"""The {param_name} you entered is invalid. \
Please use a value > 0
The Object was created with {param_name} of 1\n""")
            return 1

    def show(self) -> None:
        self._Stats.show_calls()
        print(f"{self.name}: {round(self.__height, 1)}cm, \
{round(self.__age, 1)} days old growing {round(self.__growth_rate, 1)} cm/day")

    def grow(self) -> None:
        self._Stats.grow_calls()
        self.__height += self.__growth_rate

    def age(self) -> None:
        self._Stats.age_calls()
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
        if age <= 0.0:
            print("""The Age you entered is invalid. Please use a value > 0
The Age was unchanged\n""")
        else:
            self.__age = age

    def get_stats(self):
        return self._Stats.get_stats()

# static method (self isn't passed, normal function but inside class)
    @staticmethod
    def check_age(age):
        if age <= 365:
            return False
        else:
            return True

    # Inner stats class
    class Stats():
        def __init__(self) -> None:
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0

        def grow_calls(self) -> None:
            self.__grow_calls += 1

        def age_calls(self) -> None:
            self.__age_calls += 1

        def show_calls(self) -> None:
            self.__show_calls += 1

        def get_stats(self):
            return {
                "grow calls": self.__grow_calls,
                "age calls": self.__age_calls,
                "show calls": self.__show_calls,
            }


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

    def get_bloom(self):
        return self.__bloom


# ================== SEED (SUB-FLOWER) ==================
class Seed(Flower):
    def __init__(self, name="Flower", height=1.0, age=1,
                 growth_rate=1.0, color="N/A", seeds="42") -> None:
        super().__init__(name, height, age, growth_rate, color)
        self.__seeds = seeds

    def show(self) -> None:
        super().show()
        if super().get_bloom():
            print(f"Seeds = {self.__seeds}")
        else:
            print("Seeds = 0")


#  ================== TREES ==================
class Tree(Plant):
    def __init__(self, name="Tree", height=1.0, age=1,
                 growth_rate=1.0, trunk_diameter=1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self.__trunk_dia = self.__trunk_val(trunk_diameter)
        self.__shade = False
        self._Stats: Tree.TreeStats = self.TreeStats()

    def __trunk_val(self, trunk_diameter):
        if trunk_diameter >= 0:
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
        self._Stats.shade_calls()

    def get_stats(self):
        return self._Stats.get_stats()

    # modded inner class
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self.__shade_calls = 0

        def shade_calls(self) -> None:
            self.__shade_calls += 1

        def get_stats(self):
            main_stats = super().get_stats()
            main_stats["shade calls"] = self.__shade_calls
            return main_stats


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


def ft_display_plant_stats(plant_name: Plant) -> None:
    plant_stats: dict = plant_name.get_stats()  # Recebe dict
    is_first: bool = True
    print("===== Stats ======")
    for key in plant_stats:
        value: int = plant_stats[key]
        if is_first:
            print(f"{value} {key}", end='')
            is_first = False
        else:
            print(f", {value} {key}", end='')
    print('\n')


def ft_garden_analytics() -> None:
    Rose = Flower("Rose", 2, 2, 2, "Red")
    TulipSeed = Seed("Tulip", 3, 3, 3, "Orange", 42)
    Oak = Tree("Oak", 10, 10, 10, 50.55)
    Carrot = Vegetable("Carrot", 1, 1, 1, "April", 0)
    Anon = Plant.create_anon()

    print("=== Flower ===")
    Rose.show()
    ft_display_plant_stats(Rose)
    print("=== Flower Blooming and growing/aging... ===")
    for x in range(1, 10):
        Rose.grow()
        Rose.age()
    Rose.bloom()
    Rose.show()
    ft_display_plant_stats(Rose)

    print("=== Flower Seed ===")
    TulipSeed.show()
    ft_display_plant_stats(TulipSeed)
    print("=== Flower Blooming and growing/aging... ===")
    for x in range(1, 10):
        TulipSeed.grow()
        TulipSeed.age()
    TulipSeed.bloom()
    TulipSeed.show()
    ft_display_plant_stats(TulipSeed)

    print("=== Tree ===")
    Oak.show()
    ft_display_plant_stats(Oak)
    print("=== Tree Producing shade and growing/aging... ===")
    for x in range(1, 10):
        Oak.grow()
        Oak.age()
    Oak.produce_shade()
    Oak.show()
    ft_display_plant_stats(Oak)

    print("=== Veggie ===")
    Carrot.show()
    ft_display_plant_stats(Carrot)
    print("=== Veggie growing/aging... ===")
    for x in range(1, 10):
        Carrot.grow()
        Carrot.age()
    Carrot.show()
    ft_display_plant_stats(Carrot)

    print("=== Anon Plant ===")
    Anon.show()
    ft_display_plant_stats(Anon)


if __name__ == "__main__":
    ft_garden_analytics()

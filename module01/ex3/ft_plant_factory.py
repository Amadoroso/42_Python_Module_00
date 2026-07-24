
# Defining the class plant
class Plant:
    name: str
    height: float
    aged: int  # age is a method, so i had to use aged
    growth_rate: float  # cm/day, 1 by default

    def __init__(self, name, height, aged, growth_rate=1.0) -> None:
        self.name = name
        self.height = height
        self.aged = aged
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.aged} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.aged += 1


def ft_plant_factory() -> None:

    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]
    print("=== Plant Factory Output ===")
    for x in plants:
        print("Created:", end=' ')
        x.show()


if __name__ == "__main__":
    ft_plant_factory()

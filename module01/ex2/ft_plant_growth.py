
# Defining the class plant
class Plant:
    name: str
    height: float
    aged: int  # age is a method, so i had to use aged
    growth_rate: float  # cm/day

    def __init__(self, name, height, aged, growth_rate) -> None:
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


def ft_plant_week() -> None:
    Rose = Plant("Rose", 25, 30, 0.8)
    rose_height0 = Rose.height
    print(f"""=== Garden Plant Growth ===
{Rose.name}: {round(Rose.height, 1)}cm, {Rose.aged} days old""")
    for day in range(1, 8):
        Rose.grow()
        Rose.age()
        print(f"""=== Day {day} ===
{Rose.name}: {round(Rose.height, 1)}cm, {Rose.aged} days old""")
    print(f"Growth this week: {round(Rose.height - rose_height0, 1)}cm")


if __name__ == "__main__":
    ft_plant_week()


# Defining the class plant
class Plant:
    name: str
    height: int
    age: int

    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


# Function that uses the show method i created
def ft_garden_data(Plant1: Plant, Plant2: Plant, Plant3: Plant) -> None:
    print("=== Garden Plant Registry ===")
    Plant1.show()
    Plant2.show()
    Plant3.show()


# If statement that only verifies when this file is run on its own
# The internal "__name__" object from the module (.py file)
# is assigned during runtime
if __name__ == "__main__":
    Rose: Plant = Plant("Rose", 25, 30)
    Sunflower: Plant = Plant("Sunflower", 80, 45)
    Cactus: Plant = Plant("Cactus", 15, 120)
    ft_garden_data(Rose, Sunflower, Cactus)

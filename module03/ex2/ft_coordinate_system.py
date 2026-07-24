
import math


def calc_distance(tuple_1: tuple, tuple_2: tuple) -> float:

    x: float = (tuple_2[0] - tuple_1[0])**2
    y: float = (tuple_2[1] - tuple_1[1])**2
    z: float = (tuple_2[2] - tuple_1[2])**2

    return math.sqrt(x + y + z)


def get_player_pos() -> tuple:

    while True:
        try:
            str_input: str = input("Enter new coordinates \
as floats in format 'x,y,z': ")
            str_input = str_input.replace(' ', '')
            str_div: list[str] = str_input.split(',')
            if len(str_div) != 3:
                print("Invalid Syntax")
            else:
                temp_list: list[float] = []
                for x in str_div:
                    temp_list.append(float(x))
                pos: tuple = tuple(temp_list)
                return pos
        except ValueError as e:
            print(f"Error on parameter '{x}': {e}")


def coord_printer(tuple_1: tuple) -> None:

    coord: list = ['x', 'y', 'z']
    for i in range(0, len(tuple_1)):
        if i == (len(tuple_1) - 1):
            print(f"{coord[i]}={tuple_1[i]}")
        else:
            print(f"{coord[i]}={tuple_1[i]}", end=', ')


def main() -> None:

    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    tuple_1: tuple = get_player_pos()
    print(f"Got a first tuple: {tuple_1}")
    print("It includes:", end=' ')
    coord_printer(tuple_1)
    dist_1: float = calc_distance((0, 0, 0), tuple_1)
    print(f"Distance to center: {round(dist_1, 4)}")

    print("\nGet a second set of coordinates")
    tuple_2: tuple = get_player_pos()
    dist_2: float = calc_distance(tuple_2, tuple_1)
    print(f"Distance between the 2 sets \
of coordinates: {round(dist_2, 4)}")


if __name__ == "__main__":
    main()

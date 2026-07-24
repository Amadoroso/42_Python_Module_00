
import sys


class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    END = "\033[0m"


class InvalidArgument(Exception):

    def __init__(self, message="Invalid argument"):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


class RepetitionError(Exception):

    def __init__(self, message="Redundant item"):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


def invetory_creator() -> dict[str, int]:

    inventory: dict[str, int] = dict()
    for arg in sys.argv[1:]:
        try:
            arg_div: list[str] = arg.split(':')
            if len(arg_div) != 2:
                raise InvalidArgument(f"'{Colors.BLUE}{arg}{Colors.END}' \
is an invalid argument. \
It was ignored.")
            key: str = arg_div[0]
            if key in inventory.keys():
                raise RepetitionError(f"Redundant item \
'{Colors.BLUE}{key}{Colors.END}' - discarding")
            value: int = int(arg_div[1])
            inventory[key] = value
        except ValueError:
            print(f"'{Colors.BLUE}{arg_div[1]}{Colors.END}' \
is an invalid quantity for '{Colors.BLUE}{arg_div[0]}{Colors.END}'")
        except InvalidArgument as e:
            print(e)
        except RepetitionError as e:
            print(e)

    return inventory


def item_percentage(inventory: dict[str, int]) -> None:

    for x in inventory:
        percent: float = (inventory[x]/sum(inventory.values())) * 100
        print(f"Item {x} representes: {round(percent, 1)}%")


def item_abundance(inventory: dict[str, int]) -> None:

    current_max: int = 0
    for x in inventory:
        if inventory[x] > current_max:
            current_max = inventory[x]
            max_key: str = x

    current_min = None
    for x in inventory:
        if not current_min:
            current_min = inventory[x]
            min_key: str = x
        elif inventory[x] < current_min:
            current_min = inventory[x]
            min_key = x

    print(f"Most abudant item: \
{max_key} with quantity {current_max}")
    print(f"Least abudant item: \
{min_key} with quantity {current_min}")


def item_add(inventory: dict[str, int]) -> None:

    try:
        arg: str = input("Add new item: ")
        arg_div: list[str] = arg.split(':')
        if len(arg_div) != 2:
            raise InvalidArgument(f"'{Colors.BLUE}{arg}{Colors.END}' \
is an invalid argument. \
It was ignored.")
        key: str = arg_div[0]
        if key in inventory.keys():
            raise RepetitionError(f"Redundant item \
'{Colors.BLUE}{key}{Colors.END}' - discarding")
        value: int = int(arg_div[1])
        inventory[key] = value
    except ValueError:
        print(f"'{Colors.BLUE}{arg_div[1]}{Colors.END}' \
is an invalid quantity for '{Colors.BLUE}{arg_div[0]}{Colors.END}'")
    except InvalidArgument as e:
        print(e)
    except RepetitionError as e:
        print(e)


def main() -> None:

    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print("No items provided. Usage: \
python3 ft_inventory_system.py <item_name>:<quantity>")
        return
    inventory: dict[str, int] = invetory_creator()
    if not inventory:
        print("Empty inventory...")
        return
    print(f"\nGot inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: \
{sum(inventory.values())}")
    item_percentage(inventory)
    item_abundance(inventory)
    item_add(inventory)
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()

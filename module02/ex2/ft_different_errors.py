
def garden_operations(operation_number):

    if operation_number == 0:
        return int('abc')

    elif operation_number == 1:
        return 8 / 0

    elif operation_number == 2:
        return open("file_that_doesnt_exist")

    elif operation_number == 3:
        return "ola" + 3

    print("Sucessful operation")


def test_error_types() -> None:

    try:
        garden_operations(0)
    except ValueError as error:
        print(f"A ValueError occurred: {error}")

    try:
        garden_operations(1)
    except ZeroDivisionError as error:
        print(f"A ZeroDivisionError occurred: {error}")

    try:
        garden_operations(2)
    except FileNotFoundError as error:
        print(f"A FileNotFoundErro occurred {error}")

    try:
        garden_operations(3)
    except TypeError as error:
        print(f"A TypeError occurred: {error}")

    garden_operations(4)


if __name__ == "__main__":
    test_error_types()
    print("No crash!")

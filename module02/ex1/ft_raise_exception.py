
# ValueError stores the message + the input that caused it
# All exceptions are classes that hold information
def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)

    if temp_int in range(0, 41):
        return temp_int

    elif temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")

    else:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
        # raise ValueError() inicializa um object dessa classe
        # com o conteudo que eu passei


def test_temperature() -> None:

    tests: list = ["25", "abc", "100", "-50", "40", "0"]

    for x in tests:
        try:
            print(f"\n====== testing '{x}' as an input... ======")
            input_temperature(x)
            print(f"temperatura is now {x}°C :)\n")
        except ValueError as error_message:
            print(f"input_temperature() error: {error_message}")
# except ValueError... Filtra pela class que quero.
# apanha um object da classe ValueError
# error_message passa a apontar para esse object
    print("\n No crash!")


if __name__ == "__main__":
    test_temperature()

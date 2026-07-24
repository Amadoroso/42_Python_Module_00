
def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    try:
        input_temperature("25")
        input_temperature("abc")
    except ValueError as error_message:
        print(f"input_temperature() error: {error_message}")
    print("\n No crash!")


if __name__ == "__main__":
    test_temperature()

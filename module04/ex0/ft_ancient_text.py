
import sys
import typing


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 ft_ancient_text.py <file>")
        return
    try:
        print(f"""=== Cyber Archives Recovery ===
Accessing file '{sys.argv[1]}'""")
        file: typing.IO = open(sys.argv[1], "r")
        print(f"---\n\n{file.read()}\n---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    main()

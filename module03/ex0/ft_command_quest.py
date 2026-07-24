
import sys

# sys is a built in module that is compiled in C,
# If i click in "sys" it will direct me to a .pyi which is:
# a "fake" module with information strictly for the ide
# Its an interface file thus de "i"
# The "real" sys is a built in already compiled C code inside Cpython
# I still need to import it tho, so Cpython knows it has to use it


def ft_command_quest() -> None:

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    argc: int = len(sys.argv)

    if argc == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for x in range(1, argc):
            print(f"Argument {x}: {sys.argv[x]}")

    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    ft_command_quest()

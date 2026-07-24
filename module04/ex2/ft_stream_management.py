
import sys
import typing


def reading_file() -> str:

    try:
        print(f"""=== Cyber Archives Recovery ===
Accessing file '{sys.argv[1]}'""")
        file: typing.IO = open(sys.argv[1], "r")
        content: str = file.read()
        print(f"---\n\n{content}\n---")
        file.close()
        print(f"File '{sys.argv[1]}' closed.\n")
    except FileNotFoundError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
        sys.stderr.flush()
        return ""
    except PermissionError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
        sys.stderr.flush()
        return ""
    return content


def new_file(content: str) -> None:

    try:
        print("Transform data:")
        content = content.replace('\n', '#\n')
        if content and not content.endswith('\n'):
            content = content + "#"
        print(f"---\n\n{content}\n---")
        sys.stdout.write("Enter new file name (or leave empy): ")
        sys.stdout.flush()
        new_name: str = sys.stdin.readline()
        new_name = new_name.strip()
        if not new_name:
            print("Not saving data")
            return
        print(f"Saving data to '{new_name}'")
        out_file: typing.IO = open(new_name, "w")
        out_file.write(content)
        print(f"Data saved to '{new_name}'")
        out_file.close()
    except FileNotFoundError as e:
        sys.stderr.write(f"[STDERR] Error saving to file '{new_name}': {e}\
\nNot saving data\n")
        sys.stderr.flush()
    except PermissionError as e:
        sys.stderr.write(f"[STDERR] Error saving to file '{new_name}': {e}\
\nNot saving data\n")
        sys.stderr.flush()


def main() -> None:

    if len(sys.argv) != 2:
        print("Usage: python3 ft_stream_management.py <file>")
        return
    content: str = reading_file()
    if not content:
        return
    new_file(content)


if __name__ == "__main__":
    main()

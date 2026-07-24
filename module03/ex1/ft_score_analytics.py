
import sys


def ft_score_analytics() -> None:

    print("=== Player Score Analytics ===")

    new_list: list[int] = []
    for x in sys.argv[1:]:
        try:
            new_list.append(int(x))
        except ValueError:
            print(f"Invalid Parameter: '{x}'")

    if not new_list:
        print("No scores provided. Usage: \
python3 ft_score_analytics.py <score1> <score2> ...")
        return

    new_list.sort()
    print(f"Scores Processed: {new_list}")
    print(f"Total players: {len(new_list)}")
    print(f"Total score: {sum(new_list)}")
    print(f"Average score: {sum(new_list)/len(new_list)}")
    print(f"High score: {max(new_list)}")
    print(f"Low score: {min(new_list)}")
    print(f"Score range {max(new_list) - min(new_list)}")


if __name__ == "__main__":
    ft_score_analytics()
    print()

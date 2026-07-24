
import random


class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    END = "\033[0m"


def gen_player_achievements(achiev_set: set[str]) -> set[str]:

    achiev_list = list(achiev_set)
    nbr: int = random.randrange(1, len(achiev_list))
    random_achievs: list[str] = random.sample(achiev_list, k=nbr)
    achievements: set[str] = set()
    for x in random_achievs:
        achievements.add(x)
    return achievements


def get_players() -> list[str]:

    while True:
        str_input: str = input("Please enter at least 4 unique Player names \
(format:'xx,yy,zz,ii'): ")
        str_input = str_input.replace(' ', '')
        players: list[str] = str_input.split(',')
        dup_players: set[str] = set(players)
        is_valid: bool = True
        if len(dup_players) < len(players):
            print(f"{Colors.RED}Duplicate player names detected!{Colors.END}")
            is_valid = False
        if len(players) < 4:
            print(f"{Colors.RED}Not enough player names :/{Colors.END}")
            is_valid = False
        if is_valid:
            print()
            return players


def print_achievements(player_achiev: dict[str, set[str]]) -> None:

    for x in player_achiev:
        print(f"""Player {x}:
{player_achiev[x]}\n""")


def print_distinct(player_achiev: dict[str, set[str]]) -> None:

    union = None
    for x in player_achiev:
        if not union:
            union = player_achiev[x]
        else:
            union = union.union(player_achiev[x])
    print(f"All distinct achievements: {union}\n")


def print_common(player_achiev: dict[str, set[str]]) -> None:

    shared = None
    for x in player_achiev:
        if not shared:
            shared = player_achiev[x].intersection(player_achiev[x])
        else:
            shared = shared.intersection(player_achiev[x])
    print(f"Common achievements: {shared}\n")


def print_unique(player_achiev: dict[str, set[str]]) -> None:

    for x in player_achiev:
        unique: set[str] = player_achiev[x]
        for y in player_achiev:
            if x != y:
                unique = unique.difference(player_achiev[y])
        print(f"Only {x} has: {unique}")
    print()


def print_missing(player_achiev: dict[str, set[str]],
                  achiev_set: set[str]) -> None:

    for x in player_achiev:
        print(f"{Colors.RED}{x} is missing:{Colors.END} \
{achiev_set.difference(player_achiev[x])}\n")


def main() -> None:

    achiev_set: set[str] = {
        'Crafting Genius',
        'World Savior',
        'Master Explorer',
        'Collector Supreme',
        'Untouchable',
        'Strategist',
        'Boss Slayer',
        'Sharp Mind',
        'First Steps',
        'Unstopable',
        'Hidden Path Finder',
        'Speed Runner',
    }

    print("=== Achievement Tracker System ===\n")
    players: list[str] = get_players()
    player_achiev: dict[str, set[str]] = {}
    for x in players:
        player_achiev[x] = gen_player_achievements(achiev_set)
    print_achievements(player_achiev)
    print_distinct(player_achiev)
    print_common(player_achiev)
    print_unique(player_achiev)
    print_missing(player_achiev, achiev_set)


if __name__ == "__main__":
    main()

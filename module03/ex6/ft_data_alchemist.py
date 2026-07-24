
import random


def get_players() -> list[str]:

    while True:
        arg: str = input("Please enter at least 5 player names \
(Andre,Joao,etc): ")
        if not arg:
            players: list[str] = [
                "Andre",
                "joao",
                "Carlos",
                "bruno",
                "Paulo",
                "Mario"
                ]
            print(f"Nothing was inputted. Default names assumed: {players}")
        else:
            arg = arg.replace(' ', '')
            players = arg.split(',')
        if len(players) < 5:
            print("Not enough player names...")
        for x in players:
            if not x.isalpha():
                print("Only alphabetic characters allowed...")
        else:
            return players


def all_cap(players: list[str]) -> list[str]:

    new_list: list[str] = [x.capitalize() for x in players]
    print(f"New list with all names cap. {new_list}")
    return new_list


def only_cap(players: list[str]) -> None:

    new_list: list[str] = [x for x in players if x and x[0].isupper()]
    print(f"New list of capitalized names only: {new_list}")


def gen_score() -> int:

    return random.randrange(1000)


def dict_builder(players_caps: list[str]) -> None:

    player_dict: dict[str, int] = {x: gen_score() for x in players_caps}
    print(f"Score dict: {player_dict}")
    average_score: float = sum(player_dict.values())/len(player_dict)
    print(f"Average score: {round(average_score, 2)}")
    higher_dict: dict[str, int] = {
        key: value
        for key, value in player_dict.items()
        if value > average_score
        }
    print(f"High Scores: {higher_dict}")


def main() -> None:

    players: list[str] = get_players()
    players_caps: list[str] = all_cap(players)
    only_cap(players)
    dict_builder(players_caps)


if __name__ == "__main__":
    main()

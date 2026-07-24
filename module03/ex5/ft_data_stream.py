
import random
import typing


def get_players() -> list[str]:

    while True:
        arg: str = input("Please enter some player names (xx,yy,zz,etc): ")
        if len(arg) > 0:
            arg = arg.replace(' ', '')
            players: list[str] = arg.split(',')
            return players
        else:
            print("No players, please enter player names...")


def gen_event(
        players: list[str],
        actions: list[str]
        ) -> typing.Generator[tuple[str, str], None, None]:

    while True:
        yield random.choice(players), random.choice(actions)


def event1000(
        random_event: typing.Generator[tuple[str, str], None, None]
        ) -> None:

    for x in range(1, 1001):
        event: tuple[str, str] = next(random_event)
        print(f"Random Event {x}: {event}")


def list10(
        random_event: typing.Generator[tuple[str, str], None, None]
           ) -> list[tuple[str, str]]:

    event_list: list[tuple[str, str]] = list()
    for x in range(10):
        event: tuple[str, str] = random_event.__next__()
        event_list.append(event)
    print(f"List of 10 events: {event_list}")
    return event_list


def consume_event(
        event_list: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:

    while event_list:
        event: tuple[str, str] = random.choice(event_list)
        event_list.remove(event)
        yield event


def main() -> None:

    actions: list[str] = [
        "eat",
        "sleep",
        "grab",
        "move",
        "run",
        "climb",
        "swim",
        "dance",
        "release"
    ]
    players: list[str] = get_players()
    random_event: typing.Generator = gen_event(players, actions)
    event1000(random_event)
    event_list: list[tuple[str, str]] = list10(random_event)
    for removed_event in consume_event(event_list):
        print(f"Got event from list: {removed_event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()

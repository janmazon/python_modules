import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move",
               "climb", "swim", "release"]
    while True:
        player = random.choice(players)
        action = random.choice(actions)
        yield (player, action)


def consume_event(list_event: 
    list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:
    while len(list_event) > 0:
        index = random.randint(0, len(list_event) - 1)
        yield list_event.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    gen = gen_event()
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    list_events = []
    for i in range(10):
        list_events.append(next(gen))

    print(f"Built list of 10 events: {list_events}")

    for event in consume_event(list_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_events}")


if __name__ == "__main__":
    main()

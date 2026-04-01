import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players = ["Alice", "bob", "Charlie", "dylan", "Emma",
               "Gregory", "john", "kevin", "Liam"]
    print(f"Initial list of players: {players}")
    all_capitalized = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_capitalized}")
    players_capitalized = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {players_capitalized}\n")

    scores = {name: random.randint(1, 1000) for name in all_capitalized}
    print(f"Score dict: {scores}")
    average = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")
    high = {name: score for name, score in scores.items() if score > average}
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()

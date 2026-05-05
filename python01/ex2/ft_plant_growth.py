#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days = age

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.days} days old")


def main() -> None:
    print("=== Garden Plant Growth ===")

    rose = Plant("rose", 25.0, 30)

    initial_height = round(rose.height, 1)
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.show()
        if day < 7:
            rose.grow()
            rose.age()
    print(f"Growth this week: {round(rose.height - initial_height, 1)}cm")
    print("")


if __name__ == "__main__":
    main()

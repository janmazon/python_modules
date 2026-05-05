#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self._height = 15.0
        self.set_height(height)
        self._age = 10
        self.set_age(age)

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {int(self._height)}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")

    plant = Plant("rose", 15.0, 10)

    print("Plant created: ", end="")
    plant.show()
    print("")

    plant.set_height(25.0)
    plant.set_age(30)
    print("")

    plant.set_height(-5)
    plant.set_age(-2)
    print("")

    print("Current state: ", end="")
    plant.show()


if __name__ == "__main__":
    main()

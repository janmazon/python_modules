#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: int) -> None:
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {self._height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {new_height}cm "
                  f"[REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {self._age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {new_age} [REJECTED]")
            print("Security: Negative age rejected")


def main() -> None:
    plant = SecurePlant("Rose", 25, 30)

    print("=== Garden Security System ===")
    print(f"Plant created: {plant.name}")
    plant.set_height(25)
    plant.set_age(30)
    print("")

    plant.set_height(-5)
    print("")

    print(f"Current plant: {plant.name} ({plant.get_height()}cm, "
          f"{plant.get_age()} days)")


if __name__ == "__main__":
    main()

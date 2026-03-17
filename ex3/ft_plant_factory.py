#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.days = age

    def get_info(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.days} days)")


def main() -> None:
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    print("=== Plant Factory Output ===")
    total = 0
    for plant in plants:
        plant.get_info()
        total += 1
    print("")

    print(f"Total plants created: {total}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.days = age

    def grow(self) -> None:
        self.height += 1

    def age(self) -> None:
        self.days += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.days} days old")


def main() -> None:
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    plants = [rose, sunflower, cactus]
    for plant in plants:
        initial_height = plant.height
        for day in range(1, 8):
            print(f"=== Day {day} ===")
            plant.get_info()
            if day < 7:
                plant.grow()
                plant.age()
        print(f"Growth this week: +{plant.height - initial_height}cm")
        print("")


if __name__ == "__main__":
    main()

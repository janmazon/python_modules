#!/usr/bin/env python3

from typing import Self


class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self._height = height
        self._age = age
        self._stats = self.Stats()

    def grow(self) -> None:
        self._stats._grow_calls += 1
        self._height += 8.0

    def age(self) -> None:
        self._stats._age_calls += 1
        self._age += 1

    def show(self) -> None:
        self._stats._show_calls += 1
        print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

    @staticmethod
    def validate_age(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> Self:
        return cls("Unknown plant", 0.0, 0)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.is_blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._shade_calls = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        if self.is_blooming:
            self._seeds = 42
        print(f"Seeds: {self._seeds}")


def display_stats(plant: Plant) -> None:
    print(f"[statics for {plant.name}]")
    print(f"Stats: {plant._stats._grow_calls} grow, "
          f"{plant._stats._age_calls} age, "
          f"{plant._stats._show_calls} show")
    if isinstance(plant, Tree):
        print(f" {plant._shade_calls} shade")


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.validate_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.validate_age(400)}")
    print("")

    rose = Flower("rose", 15.0, 10, "red")
    oak = Tree("oak", 200.0, 365, 5.0)
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    anonymous = Plant.anonymous()

    print("=== Flower")
    rose.show()
    display_stats(rose)
    print(f"[asking the {rose.name.lower()} to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stats(rose)
    print("")

    print("=== Tree")
    oak.show()
    display_stats(oak)
    print(f"[asking the {oak.name.lower()} to produce shade]")
    oak.produce_shade()
    display_stats(oak)
    print("")

    print("=== Seed")
    sunflower.show()
    print(f"[make {sunflower.name.lower()} grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    print("")

    print("=== Anonymous")
    anonymous.show()
    display_stats(anonymous)


if __name__ == "__main__":
    main()

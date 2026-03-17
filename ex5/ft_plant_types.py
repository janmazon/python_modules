#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str, ) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")
        print(f"{self.name} is blooming beautifully!")
        print("")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade_area = self.trunk_diameter * 1.56
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {int(shade_area)} square meters of shade")
        print("")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def print_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")
        print("")


def main() -> None:
    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 80, 45, "yellow")
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 350, 978, 27)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 30, 50, "autumn", "vitamin A")

    print("=== Garden Plant Types ===")
    print("")

    rose.bloom()
    sunflower.bloom()
    oak.produce_shade()
    pine.produce_shade()
    tomato.print_info()
    carrot.print_info()


if __name__ == "__main__":
    main()

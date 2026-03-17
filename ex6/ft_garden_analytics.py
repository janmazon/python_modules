#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self) -> None:
        self.height += 1

    def get_info(self) -> None:
        return (f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> None:
        return super().get_info() + (f", {self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str,
                 points: int) -> None:
        super().__init__(name, height, color)
        self.points = points

    def get_info(self) -> None:
        return super().get_info() + (f", Prize points: {self.points}")


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants: list[Plant] = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)

    def help_plants_grow(self) -> None:
        for plant in self.plants:
            plant.grow()


class GardenManager:
    total_gardens = 0

    def __init__(self) -> None:
        self.gardens = []

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls):
        return cls()

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    class GardenStats:
        @staticmethod
        def get_plant_types(garden: Garden) -> list:
            regular = 0
            flowering = 0
            prize = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                elif isinstance(plant, Plant):
                    regular += 1
            return regular, flowering, prize

        @staticmethod
        def calculate_score(garden: Garden) -> int:
            score = 0
            for plant in garden.plants:
                score += 10 + plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.points
            return score


def main() -> None:
    print("=== Garden Management System Demo ===")
    print("")

    manager = GardenManager.create_garden_network()
    alice_garden = Garden("Alice")
    bob_garden = Garden("Bob")
    manager.add_garden(alice_garden)
    manager.add_garden(bob_garden)

    bob_secret_plant = Plant("Bonsai", 82)
    bob_garden.add_plant(bob_secret_plant)

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
    plants: list[Plant] = [oak, rose, sunflower]
    for plant in plants:
        alice_garden.add_plant(plant)
        print(f"Added {plant.name} to {alice_garden.owner}'s garden")
    print("")

    print(f"{alice_garden.owner} is helping all plants grow...")
    alice_garden.help_plants_grow()
    for plant in alice_garden.plants:
        print(f"{plant.name} grew 1cm")
    print("")

    print(f"=== {alice_garden.owner}'s Garden Report ===")
    print("Plants in garden:")
    for plant in alice_garden.plants:
        print(f"{plant.get_info()}")
    print("")

    total_plants = len(alice_garden.plants)
    total_growth = total_plants
    print(f"Plants added: {total_plants}, Total growth: {total_growth}cm")
    reg, flow, pri = GardenManager.GardenStats.get_plant_types(alice_garden)
    print(f"Plant types: {reg} regular, {flow} flowering, {pri} prize flowers")
    print("")

    is_valid = GardenManager.validate_height(oak.height)
    print(f"Height validation test: {is_valid}")
    alice_score = GardenManager.GardenStats.calculate_score(alice_garden)
    bob_score = GardenManager.GardenStats.calculate_score(bob_garden)
    print(f"Garden scores - {alice_garden.owner}: {alice_score}, "
          f"{bob_garden.owner}: {bob_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()

from ex0.creature import Creature
from ex0.factories import CreatureFactory
from .capabilities import HealCapability


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Sproutling", "Grass")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return (f'{self.name} uses Vine Whip!')

    def heal(self) -> str:
        return (f'{self.name} heals itself for a small amount')


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Bloomelle", "Grass/Fairy")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return (f'{self.name} uses Petal Dance!')

    def heal(self) -> str:
        return (f'{self.name} heals itself and others for a large amount')


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling()

    def create_evolved(self) -> Bloomelle:
        return Bloomelle()

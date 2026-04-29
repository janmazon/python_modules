from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import TransformCapability, HealCapability
from typing import cast


class StrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            return creature.attack()
        else:
            raise StrategyError(f"Invalid Creature '{creature.name}' for "
                                f"this normal strategy")


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            creature_cast = cast(TransformCapability, creature)
            aggressive = [
                creature_cast.transform(),
                creature.attack(),
                creature_cast.revert()
            ]
            return "\n".join(aggressive)
        else:
            raise StrategyError(f"Invalid Creature '{creature.name}' for "
                                f"this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            creature_cast = cast(HealCapability, creature)
            defensive = [
                creature.attack(),
                creature_cast.heal(),
            ]
            return "\n".join(defensive)
        else:
            raise StrategyError(f"Invalid Creature '{creature.name}' for "
                                f"this defensive strategy")

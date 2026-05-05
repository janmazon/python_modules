from ex0.creature import Creature
from ex0.factories import CreatureFactory, FlameFactory, AquaFactory
from ex1.healingfactory import HealingCreatureFactory
from ex1.transformfactory import TransformCreatureFactory
from ex2.strategy import BattleStrategy, StrategyError
from ex2.strategy import NormalStrategy, DefensiveStrategy, AggressiveStrategy


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    try:
        participants: list[tuple[Creature, BattleStrategy]] = []
        opponents_list: list[str] = []
        names: dict[str, str] = {
            "FlameFactory": "Flameling",
            "AquaFactory": "Aquabub",
            "HealingCreatureFactory": "Healing",
            "TransformCreatureFactory": "Transform"
        }
        for factory, strategy in opponents:
            creature = factory.create_base()
            participants.append((creature, strategy))

            factory_name = factory.__class__.__name__
            factory_name = names.get(factory_name, factory_name)
            strategy_name = strategy.__class__.__name__.replace("Strategy", "")
            opponents_list.append(f"({factory_name}+{strategy_name})")

        print(f" [ {", ".join(opponents_list)} ]")
        print("*** Tournament ***")
        print(f"{len(participants)} opponents involved")

        for i in range(len(participants)):
            for j in range(i + 1, len(participants)):
                criature1, strategy1 = participants[i]
                criature2, strategy2 = participants[j]

                print("\n* Battle *")
                print(f"{criature1.describe()}")
                print(" vs.")
                print(f"{criature2.describe()}")
                print(" now fight!")

                print(strategy1.act(criature1))
                print(strategy2.act(criature2))

    except StrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


if __name__ == "__main__":
    tournament0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    print("Tournament 0 (basic)")
    battle(tournament0)

    tournament1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    print("\nTournament 1 (error)")
    battle(tournament1)

    tournament2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    print("\nTournament 2 (multiple)")
    battle(tournament2)

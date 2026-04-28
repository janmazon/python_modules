from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factories(factory: CreatureFactory) -> None:
    try:
        base = factory.create_base()
        evolved = factory.create_evolved()
        print("Testing factory")
        print(f"{base.describe()}")
        print(f"{base.attack()}")
        print(f"{evolved.describe()}")
        print(f"{evolved.attack()}\n")
    except Exception as e:
        print(f"Error {e}")


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    try:
        base1 = factory1.create_base()
        base2 = factory2.create_base()
        print("Testing battle")
        print(f"{base1.describe()}")
        print(" vs.")
        print(f"{base2.describe()}")
        print(" fight!")
        print(f"{base1.attack()}")
        print(f"{base2.attack()}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_factories(FlameFactory())
    test_factories(AquaFactory())
    test_battle(FlameFactory(), AquaFactory())

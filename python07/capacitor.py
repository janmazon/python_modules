from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing() -> None:
    try:
        factory = HealingCreatureFactory()
        base = factory.create_base()
        evolved = factory.create_evolved()
        print("Testing Creature with healing capability")
        print(" base:")
        print(f"{base.describe()}")
        print(f"{base.attack()}")
        print(f"{base.heal()}")
        print(" evolved:")
        print(f"{evolved.describe()}")
        print(f"{evolved.attack()}")
        print(f"{evolved.heal()}\n")
    except Exception as e:
        print(f"Error {e}")


def test_transform() -> None:
    try:
        factory = TransformCreatureFactory()
        base = factory.create_base()
        evolved = factory.create_evolved()
        print("Testing Creature with transform capability")
        print(" base:")
        print(f"{base.describe()}")
        print(f"{base.attack()}")
        print(f"{base.transform()}")
        print(f"{base.attack()}")
        print(f"{base.revert()}")
        print(" evolved:")
        print(f"{evolved.describe()}")
        print(f"{evolved.attack()}")
        print(f"{evolved.transform()}")
        print(f"{evolved.attack()}")
        print(f"{evolved.revert()}")
    except Exception as e:
        print(f"Error {e}")


if __name__ == "__main__":
    test_healing()
    test_transform()

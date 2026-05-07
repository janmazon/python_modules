from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    amount = initial_power

    def accumulates(power: int) -> int:
        nonlocal amount
        amount += power
        return amount
    return accumulates


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    storage: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key: str) -> Any:
        return storage.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    initial_power = 100
    acumulator = spell_accumulator(initial_power)
    print(f"Base {initial_power}, add 20: {acumulator(20)}")
    print(f"Base {initial_power}, add 30: {acumulator(30)}")

    print("\nTesting enchantment factory...")
    factory1 = enchantment_factory("Flaming")
    factory2 = enchantment_factory("Frozen")
    print(f"{factory1('Sword')}")
    print(f"{factory2('Shield')}")

    print("\nTesting memory vault...")
    vault = memory_vault()
    key = "secret"
    value = 42
    vault['store'](key, value)
    print(f"Store '{key}' = {value}")
    print(f"Recall '{key}': {vault['recall'](key)}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()

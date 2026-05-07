from collections.abc import Callable
from typing import Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(lambda a, b: a if a > b else b, spells)
    elif operation == "min":
        return reduce(lambda a, b: a if a < b else b, spells)
    else:
        raise ValueError("Unknown operation")


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "Fire": partial(base_enchantment, power=50, element="Fire"),
        "Water": partial(base_enchantment, power=50, element="Water"),
        "Air": partial(base_enchantment, power=50, element="Air")
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment hits {target} with {power} power"


def main() -> None:
    spell_powers = [49, 27, 12]

    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")

    print("\nTesting partial enchanter...")
    enchanment = partial_enchanter(base_enchantment)
    print(f"{enchanment['Fire'](target='Sword')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"{dispatcher(42)}")
    print(f"{dispatcher('fireball')}")
    print(f"{dispatcher(spell_powers)}")
    print(f"{dispatcher(1.3)}")


if __name__ == "__main__":
    main()

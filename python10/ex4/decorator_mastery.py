from functools import wraps
from collections.abc import Callable
from typing import Any
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start

        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            if 'power' in kwargs:
                power = kwargs['power']
            else:
                power = next((a for a in args if isinstance(a, int)), None)
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {attempt}/{max_attempts})")
            return (f"Spell casting failed after {max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


def main() -> None:
    @spell_timer
    def fireball(target: str, power: int) -> str:
        time.sleep(0.1)
        return (f"Fireball hits {target} for {power} damage")

    print("Testing spell timer...")
    result = fireball("Dragon", 50)
    print(f"Result: {result}")

    @power_validator(20)
    def cast(power: int, target: str) -> str:
        return f"Spell hits {target} with {power} power"

    print("\nTesting power validator...")
    print(cast(30, "Dragon"))
    print(cast(10, "Dragon"))

    @retry_spell(3)
    def unstable_spell() -> str:
        raise Exception("Spell unstable!")

    print("\nTesting retrying spell...")
    result = unstable_spell()
    print(result)
    print("Waaaaaaagh spelled !")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(f"{MageGuild.validate_mage_name('Jordan')}")
    print(f"{MageGuild.validate_mage_name('Jo')}")
    print(f"{guild.cast_spell('Lightning', 15)}")
    print(f"{guild.cast_spell('Lightning', 5)}")


if __name__ == "__main__":
    main()

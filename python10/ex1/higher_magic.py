from _collections_abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def mega_fireball(target: str, power: int) -> str: 
        return base_spell(target, power * multiplier)
    return mega_fireball


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzed"
    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        sequence: list[str] = []
        for spell in spells:
            sequence.append(spell(target, power))
        return sequence
    return sequence_spell


def main() -> None:
    print("\nTesting spell combiner...")


if __name__ == "__main__":
    main()

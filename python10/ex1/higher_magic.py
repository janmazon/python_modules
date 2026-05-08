from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
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
    combo = spell_combiner(fireball, heal)
    result_combo1, result_combo2 = combo("Dragon", 10)
    print(f"Combined spell result: {result_combo1}, {result_combo2}")

    print("\nTesting power amplifier...")
    result_base = fireball("Dragon", 10)
    ampli = power_amplifier(fireball, 3)
    result_ampli = ampli("Dragon", 10)
    print(f"Original: {result_base}")
    print(f"Amplified: {result_ampli}")

    print("\nTesting conditional caster...")
    result_caster1 = conditional_caster(lambda _, power: power >= 20, heal)
    result_caster2 = conditional_caster(lambda _, power: power >= 20, fireball)
    print(result_caster1("Dragon", 30))
    print(result_caster2("Dragon", 10))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    result_sequence = sequence("Dragon", 10)
    print("Spell sequence result (list):")
    for spell in result_sequence:
        print(f"{spell}")


if __name__ == "__main__":
    main()

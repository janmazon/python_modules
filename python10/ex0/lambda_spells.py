def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return list(sorted(artifacts, key=lambda m: m['power'], reverse=True))


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: '* ' + s + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    most_powerful = max(mages, key=lambda m: m['power'])['power']
    least_powerful = min(mages, key=lambda m: m['power'])['power']
    powers = list(map(lambda m: m['power'], mages))
    average = round(sum(powers) / len(powers), 2)
    return {'max_power': most_powerful, 'min_power': least_powerful, 
            'avg_power': average}


def main() -> None:
    artifacts = [
        {'name': 'Crystal Orb', 'power': 106, 'type': 'relic'},
        {'name': 'Storm Crown', 'power': 63, 'type': 'accessory'},
        {'name': 'Fire Staff', 'power': 119, 'type': 'armor'},
        {'name': 'Light Prism', 'power': 93, 'type': 'weapon'}
    ]
    mages = [
        {'name': 'Sage', 'power': 99, 'element': 'light'},
        {'name': 'Nova', 'power': 89, 'element': 'wind'},
        {'name': 'Ember', 'power': 98, 'element': 'shadow'},
        {'name': 'Alex', 'power': 86, 'element': 'ice'},
        {'name': 'Luna', 'power': 88, 'element': 'wind'}
    ]
    spells = ['flash', 'blizzard', 'shield', 'heal']

    print("\nTesting artifact sorter...")
    sorted_artifact = artifact_sorter(artifacts)
    for i in range(len(sorted_artifact) - 1):
        art1 = sorted_artifact[i]
        art2 = sorted_artifact[i + 1]
        print(f"{art1['name']} ({art1['power']} power) comes before "
              f"{art2['name']} ({art2['power']} power)")

    print("\nTesting spell transformer...")
    print(*spell_transformer(spells))

    print("\nTesting power filter...")
    filter_power = power_filter(mages, 90)
    for mage in filter_power:
        print(f"{mage['name']} ({mage['power']} power)")

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max power: {stats['max_power']} power")
    print(f"Min power: {stats['min_power']} power")
    print(f"Average power: {stats['avg_power']} power")


if __name__ == '__main__':
    main()

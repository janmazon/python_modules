import random


def gen_player_achievements(achievements_list: list[str]) -> set[str]:
    quantity = random.randint(1, 15)
    selection = random.sample(achievements_list, quantity)
    return set(selection)


def main() -> None:
    print("=== Achievement Tracker System ===\n")

    achievements_list = [
        'Crafting Genius', 'World Savior', 'Master Explorer',
        'Collector Supreme', 'Untouchable', 'Boss Slayer', 'Strategist',
        'Unstoppable', 'Speed Runner', 'Survivor', 'Treasure Hunter',
        'First Steps', 'Sharp Mind', 'Hidden Path Finder', 'Legendary Hero'
    ]

    alice_set = gen_player_achievements(achievements_list)
    bob_set = gen_player_achievements(achievements_list)
    charl_set = gen_player_achievements(achievements_list)
    dylan_set = gen_player_achievements(achievements_list)

    print(f"Player Alice: {alice_set}")
    print(f"Player Bob: {bob_set}")
    print(f"Player Charlie: {charl_set}")
    print(f"Player Dylan: {dylan_set}\n")

    all_achievements = alice_set | bob_set | charl_set | dylan_set
    common = alice_set & bob_set & charl_set & dylan_set
    total_list = set(achievements_list)

    print(f"All distinct achievements: {all_achievements}\n")

    print(f"Common achievements: {common}\n")

    print(f"Only Alice has: {alice_set - (bob_set | charl_set | dylan_set)}")
    print(f"Only Bob has: {bob_set - (alice_set | charl_set | dylan_set)}")
    print(f"Only Charlie has: {charl_set - (alice_set | bob_set | dylan_set)}")
    print(f"Only Dylan has: {dylan_set - (alice_set | bob_set | charl_set)}\n")

    print(f"Alice is missing: {total_list - alice_set}")
    print(f"Bob is missing: {total_list - bob_set}")
    print(f"Charlie is missing: {total_list - charl_set}")
    print(f"Dylan is missing: {total_list - dylan_set}")


if __name__ == "__main__":
    main()

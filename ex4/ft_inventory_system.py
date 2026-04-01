import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory = {}
    for i in range(1, len(sys.argv)):
        args = sys.argv[i]
        parts = args.split(":")
        if len(parts) == 2:
            item = parts[0]
            input_value = parts[1]
            if item in inventory:
                print(f"Redundant item '{item}' - discarding")
            else:
                try:
                    inventory[item] = int(input_value)
                except ValueError as e:
                    print(f"Quantity error for '{item}': {e}")
        else:
            print(f"Error - invalid parameter '{args}'")
    if not inventory:
        return

    print(f"Got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")
    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    most_abundant = item_list[0]
    least_abundant = item_list[0]

    for item in inventory:
        percentage = (inventory[item] / total_quantity) * 100
        print(f"Item {item} represents {round(percentage, 1)}%")
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item
        if inventory[item] < inventory[least_abundant]:
            least_abundant = item

    print(f"Item most abundant: {most_abundant} "
          f"with quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant} "
          f"with quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()

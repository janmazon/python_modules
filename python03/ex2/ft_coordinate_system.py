import math


def get_player_pos() -> tuple:
    while True:
        user_input = input("Enter new coordinates as "
                           "floats in format 'x,y,z': ")
        coordinates = user_input.split(",")
        if len(coordinates) == 3:
            try:
                x = float(coordinates[0])
                y = float(coordinates[1])
                z = float(coordinates[2])
                return x, y, z
            except ValueError:
                for c in coordinates:
                    try:
                        float(c)
                    except ValueError as e:
                        print(f"Error on parameter '{c}': {e}")
                        break
        else:
            print("Invalid syntax")


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    get_input1 = get_player_pos()
    x1, y1, z1 = get_input1
    print(f"Got a first tuple: {get_input1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: "
          f"{round(math.sqrt(x1**2 + y1**2 + z1**2), 4)}\n")

    print("Get a second set of coordinates")
    get_input2 = get_player_pos()
    x2, y2, z2 = get_input2
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 4)}")


if __name__ == "__main__":
    main()

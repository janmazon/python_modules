#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")

    valid_input = "25"
    print(f"Input data is '{valid_input}'")
    temp = input_temperature(valid_input)
    print(f"Temperature is now {temp}°C\n")

    error_input = "abc"
    print(f"Input data is '{error_input}'")
    try:
        input_temperature(error_input)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

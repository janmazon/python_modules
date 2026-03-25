#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")

    valid_input = "25"
    print(f"Input data is '{valid_input}'")
    temperature = input_temperature(valid_input)
    print(f"Temperature is now {temperature}°C\n")

    error_input = "abc"
    print(f"Input data is '{error_input}'")
    try:
        input_temperature(error_input)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    max_temperature = "100"
    print(f"Input data is '{max_temperature}'")
    try:
        input_temperature(max_temperature)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    min_temperature = "-50"
    print(f"Input data is '{min_temperature}'")
    try:
        input_temperature(min_temperature)
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = []
    for i in range(1, len(sys.argv)):
        argument = sys.argv[i]
        try:
            number = int(argument)
            scores.append(number)
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")

    if not scores:
        print(f"No scores provided. "
              f"Usage: python3 {sys.argv[0]} <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {round(sum(scores) / len(scores), 1)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()

import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    id = str(input("Input Stream active. Enter archivist ID: "))
    report = str(input("Input Stream active. Enter status report: "))

    print(f"\n[STANDARD] Archive status from {id}: {report}", file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels "
          "verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    main()

def handle_errors(file_name: str) -> None:
    if file_name == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{file_name}'")
    else:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'")

    try:
        with open(file_name, "r") as vault:
            content = vault.read()
            print(f"SUCCESS: Archive recovered - ''{content}''")
            print("STATUS: Normal operations resumed\n")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception as e:
        print(f"RESPONSE: Unexpected system anomaly - {e}")
        print("STATUS: Emergency protocols active\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    handle_errors("lost_archive.txt")
    handle_errors("classified_vault.txt")
    handle_errors("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()

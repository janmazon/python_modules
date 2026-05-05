def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    vault_name = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {vault_name}")
    try:
        vault = open(vault_name, "r")
        print("Connection established...\n")

        print("RECOVERED DATA:")
        content = vault.read()
        print(f"{content}\n")

        vault.close()
        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    main()

def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("\nSECURE EXTRACTION:")
    try:
        with open("classified_data.txt", "r") as vault:
            content = vault.read()
            print(content)

        print("\nSECURE PRESERVATION:")
        with open("security_protocols.txt", "w") as vault:
            vault.write("[CLASSIFIED] New security protocols archived\n")

        with open("security_protocols.txt", "r") as vault:
            content = vault.read()
            print(content, end="")

        print("Vault automatically sealed upon completion\n")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()

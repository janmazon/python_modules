def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    vault_name = "new_discovery.txt"
    print(f"Initializing new storage unit: {vault_name}")
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")
    new_file = open(vault_name, "w")
    lines = ["[ENTRY 001] New quantum algorithm discovered",
             "[ENTRY 002] Efficiency increased by 347%",
             "[ENTRY 003] Archived by Data Archivist trainee"
             ]
    for line in lines:
        new_file.write(f"{line}\n")
        print(line)
    new_file.close()

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{vault_name}' ready for long-term preservation.")


if __name__ == "__main__":
    main()

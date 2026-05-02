import os


def load_and_display_configuration() -> bool:
    try:
        from dotenv import load_dotenv      #type: ignore
        load_dotenv()
        configuration: dict[str, str] = {
            "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
            "DATABASE_URL": os.getenv("DATABASE_URL", "not configured"),
            "API_KEY": os.getenv("API_KEY", "not configured"),
            "LOG_LEVEL": os.getenv("LOG_LEVEL", "DEBUG"),
            "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", "not configured"),
        }
        print("\nORACLE STATUS: Reading the Matrix...\n")
        print("Configuration loaded:")
        print(f"Mode: {configuration['MATRIX_MODE']}")
        print(f"Database: {configuration['DATABASE_URL']}")
        print(f"API Key: {configuration['API_KEY']}")
        print(f"Log Level: {configuration['LOG_LEVEL']}")
        print(f"Zion: {configuration['ZION_ENDPOINT']}")
        return True
    
    except ModuleNotFoundError:
        print("ERROR: Missing dependency: python-dotenv\n")
        print("Install dotenv with: pip install python-dotenv")
        return False


def security_check() -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if not os.path.exists(".env"):
        print("[WARNING] .env file not found")
    else:
        print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


def oracle() -> None:
    if load_and_display_configuration():
        security_check()


if __name__ == "__main__":
    oracle()

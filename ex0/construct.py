import sys
import os
import site


def construct() -> None:
    is_venv = sys.prefix != sys.base_prefix
    if not is_venv:
        print("\nMATRIX STATUS: You're still plugged in\n")

        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print(r"matrix_env\Scripts\activate # On Windows" + "\n")

        print("Then run this program again.")
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")

        venv_name = os.path.basename(sys.prefix)
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {sys.prefix}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")

        package_path = site.getsitepackages()[0]
        print("Package installation path:")
        print(f"{package_path}")


if __name__ == "__main__":
    construct()
import os
import sys
from time import sleep

# Current version of the script
LATEST_VERSION = "0.0.3"  # Update this manually when releasing a new version
VERSION_FILE = "version.txt"  # File to store the last executed version


def check_for_updates():
    
    print("Checking for updates...")
    sleep(1)

    # Simulated latest version for testing
    latest_version = LATEST_VERSION  # Replace with an actual versioning mechanism if needed

    # Check if version file exists
    if os.path.exists(VERSION_FILE):
        with open(VERSION_FILE, "r") as f:
            stored_version = f.read().strip()
    else:
        # If the file doesn't exist, create it and write the current version
        print(f"{VERSION_FILE} does not exist. Creating it...")
        with open(VERSION_FILE, "w") as f:
            f.write("0")
        print(f"Stored the current version as 0 in {VERSION_FILE}.")
        stored_version = "0"

    # Compare stored version with the current version
    if stored_version != latest_version:
        print(f"A new version ({latest_version}) is available!")
        choice = input("Do you want to update? (y/n): ").strip().lower()
        if choice == "y":
            print("Updating...")
            # Update the version file with the current version
            with open(VERSION_FILE, "w") as f:
                f.write(LATEST_VERSION)
            print("Updated version file with the current version.")

            # Perform the update here. This can be downloading a new executable, etc.

            print("Please download the updated executable.")
        else:
            print("Skipping update. You can continue using the current version.")
    else:
        print("You are using the latest version.")


def setup_files():
    """Sets up required files."""
    print("Setting up required files...")
    files = ["config.json", "emails.csv", "proxies.txt"]
    folders = ["events"]

    for file in files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                if file == "emails.csv":
                    f.write("email\n")
                elif file == "config.json":
                    f.write("{}")

    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    print("Setup completed. You can now use the application!")


def main_menu():
    """Displays the main menu."""
    while True:
        os.system("clear")  # Clear the screen for a clean display
        print(logo_color + logo + reset_color)
        print(f"Version: {LATEST_VERSION}")
        print("--- MAIN MENU ---")
        print("1. Enter Signups")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            signups_menu()
        elif choice == "0":
            sys.exit("Goodbye!")
        else:
            print("Invalid choice. Please try again.")
            sleep(1)


def signups_menu():
    """Displays the signups menu."""
    while True:
        os.system("clear")  # Clear the screen for a clean display
        print(logo_color + logo + reset_color)
        print("--- SIGNUPS MENU ---")
        print("1. Charli xcxc Signup")
        print("2. FIFA 2025 Signup")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("Coldplay Signup selected.")
            sleep(2)
        elif choice == "2":
            print("FIFA 2025 Signup selected.")
            sleep(2)
        elif choice == "0":
            return
        else:
            print("Invalid choice. Please try again.")
            sleep(1)


# ASCII logo for the app
logo = """
     _______. __    _______ .__   __.  __   ___________    ____
    /       ||  |  /  _____||  \\ |  | |  | |   ____\\   \\  /   /
   |   (----`|  | |  |  __  |   \\|  | |  | |  |__   \\   \\/   /
    \\   \\    |  | |  | |_ | |  . `  | |  | |   __|   \\_    _/
.----)   |   |  | |  |__| | |  |\\   | |  | |  |        |  |
|_______/    |__|  \\______| |__| \\__| |__| |__|        |__|
"""
logo_color = "\033[95m"
reset_color = "\033[0m"


def main():
    """Main entry point of the program."""
    print(logo_color + logo + reset_color)
    print("Welcome to Signify!")
    sleep(1)

    # Check for updates when the app starts
    check_for_updates()

    # Set up required files
    setup_files()

    # Launch the main menu
    main_menu()


if __name__ == "__main__":
    main()

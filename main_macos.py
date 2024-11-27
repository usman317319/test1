import os
import sys
import requests
from time import sleep
import subprocess

# URLs for version checking and executable download
VERSION_CHECK_URL = "https://raw.githubusercontent.com/ScriptTommy/Python-Script-Windows/main/version.txt"
EXE_DOWNLOAD_URL = "https://raw.githubusercontent.com/ScriptTommy/Python-Script-Windows/main/Signify.exe"
EXE_NAME = "Signify.exe"  # Current executable name for Windows

# Current version embedded in the script
CURRENT_VERSION = "0.0.1"  # Update this manually in the script for new versions

# Colors
gradient_border = ["\033[38;5;128m", "\033[38;5;129m", "\033[38;5;201m", "\033[38;5;213m"]  # Purple to Neon Pink gradient
electric_purple = "\033[38;5;93m"  # Electric Purple for Signify Menu
cyan = "\033[38;5;51m"  # Cyan for options
reset = "\033[0m"  # Reset color
white = ""  # Default terminal color

# ASCII logo
logo = r"""
     _______. __    _______ .__   __.  __   ___________    ____
    /       ||  |  /  _____||  \ |  | |  | |   ____\   \  /   /
   |   (----`|  | |  |  __  |   \|  | |  | |  |__   \   \/   /
    \   \    |  | |  | |_ | |  . `  | |  | |   __|   \_    _/
.----)   |   |  | |  |__| | |  |\   | |  | |  |        |  |
|_______/    |__|  \______| |__| \__| |__| |__|        |__|
"""

# Gradient border function
def gradient_line(width=50):
    """Creates a gradient border of a specified width."""
    return "".join(gradient_border[i % len(gradient_border)] + "═" for i in range(width)) + reset


def check_for_updates():
    """Check online for updates."""
    try:
        # Fetch the latest version number from the server
        response = requests.get(VERSION_CHECK_URL)
        response.raise_for_status()
        latest_version = response.text.strip()

        if latest_version != CURRENT_VERSION:
            os.system("cls" if os.name == "nt" else "clear")
            print(electric_purple + logo + reset)  # Show logo
            print(f"\nA new version ({latest_version}) is available!")
            choice = input(f"Do you want to update to version {latest_version}? (y/n): ").strip().lower()
            if choice == "y":
                download_and_replace_exe(latest_version)
            else:
                print("Update skipped. You will be prompted again next time.")
                sleep(2)
        else:
            print(f"{cyan}You are already using the latest version ({CURRENT_VERSION}).{reset}")
            sleep(2)
    except Exception as e:
        print(f"{white}Error checking for updates: {e}{reset}")
        sleep(2)


def download_and_replace_exe(new_version):
    """Download and replace the current executable with the latest version."""
    print(f"{white}Downloading the latest version...{reset}")
    try:
        print(f"DEBUG: Downloading to: {os.path.abspath(EXE_NAME)}")
        response = requests.get(EXE_DOWNLOAD_URL, stream=True)
        response.raise_for_status()

        with open(EXE_NAME, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        os.chmod(EXE_NAME, 0o755)

        print(f"{cyan}Update to version {new_version} was successful. Restarting application...{reset}")
        sleep(2)

        absolute_path = os.path.abspath(EXE_NAME)
        if os.path.exists(absolute_path) and os.access(absolute_path, os.X_OK):
            subprocess.Popen([absolute_path], shell=False)
            sys.exit(0)
        else:
            print(f"{white}Failed to restart. File not found or not executable.{reset}")
    except Exception as e:
        print(f"{white}Failed to update: {e}{reset}")
        sleep(2)


def menu():
    """Display the main menu with a fixed box and consistent alignment."""
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        # Show logo
        print(electric_purple + logo + reset)

        # Calculate the box width dynamically based on content
        box_width = 50  # Fixed width for the box
        spacer = " " * (box_width - 2)  # Space padding for empty lines
        version_text = f"Version: {CURRENT_VERSION}"
        title_text = "Signify Menu"
        option_text = [
            "1. Charclicx",
            "2. Taylor Swift",
            "3. Coldplay",
            "0. Exit"
        ]

        # Top border
        print(f"{gradient_border[0]}╔{gradient_line(box_width)}╗{reset}")

        # Title
        print(f"{gradient_border[1]}║ {electric_purple}{title_text.center(box_width - 2)}{reset} {gradient_border[1]}║{reset}")

        # Version
        print(f"{gradient_border[2]}║ {electric_purple}{version_text.center(box_width - 2)}{reset} {gradient_border[2]}║{reset}")

        # Divider
        print(f"{gradient_border[3]}╠{gradient_line(box_width)}╣{reset}")

        # Menu options
        for i, option in enumerate(option_text):
            color = cyan
            print(f"{gradient_border[i % len(gradient_border)]}║ {color}{option.ljust(box_width - 2)}{reset} {gradient_border[i % len(gradient_border)]}║{reset}")

        # Bottom border
        print(f"{gradient_border[0]}╚{gradient_line(box_width)}╝{reset}")

        # User input
        choice = input(f"{white}Enter your choice: {reset}").strip()

        if choice == "1":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{cyan}Charclicx functionality coming soon...{reset}")
            sleep(2)
        elif choice == "2":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{cyan}Taylor Swift functionality coming soon...{reset}")
            sleep(2)
        elif choice == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{cyan}Coldplay functionality coming soon...{reset}")
            sleep(2)
        elif choice == "0":
            sys.exit(f"{white}Goodbye!{reset}")
        else:
            print(f"{white}Invalid choice. Please try again.{reset}")
            sleep(2)


if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    check_for_updates()  # Check for updates at startup
    menu()  # Launch the menu
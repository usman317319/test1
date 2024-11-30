import os
import sys
import requests
from time import sleep
import shutil
import subprocess
import threading

# Current version of the script
CURRENT_VERSION = "0.0.3"

if os.path.exists("launcher.bat"):
    os.remove("launcher.bat")

# Returns the contents of version.txt file from github repo
def fetch_version_from_github():
    """Fetch a file's contents from a GitHub repository."""
    # url = f"https://api.github.com/repos/ScriptTommy/Python-Script-Windows/contents/version.txt?ref=main"
    url = f"https://api.github.com/repos/usman317319/test1/contents/version.txt?ref=main"
    headers = {}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.json()
        # Decode the base64-encoded content
        from base64 import b64decode
        file_content = b64decode(content["content"]).decode("utf-8")
        return file_content.strip()
    else:
        print(f"Failed to fetch Version")

# Downloads the Executable from GitHub
def download_executable():
    """Download the file from the given URL and save it as a temporary file."""
    try:
        url = "https://raw.githubusercontent.com/usman317319/test1/main/Signify.py"
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            with open("Signify.py", 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):  # Process the response in chunks
                    file.write(chunk)

            print(f"File downloaded successfully")
        else:
            print(f"Failed to download file: {response.status_code} - {response.text}")
            sys.exit(1)
    except Exception as e:
        print(f"Error downloading file: {e}")
        sys.exit(1)

# Another Process in a separate thread is initiated which will then delete, rename and Execute the new executble
def hand_over(latest_version):
    # Write the launcher script
    current_exe_name = os.path.basename(sys.argv[0]).replace(".py", ".exe")
    with open("launcher.bat", "w") as launcher:
        launcher.write(f"""
        timeout /t 1 >nul
        del {current_exe_name}
        pyinstaller --onefile Signify.py
        start .\dist\Signify.exe
        cls
        """)

    global CURRENT_VERSION
    CURRENT_VERSION = latest_version
    subprocess.Popen(["cmd", "/c", "start", "launcher.bat"])
    os._exit(0)

def check_for_updates():
    
    print("Checking for updates...")

    # Simulated latest version for testing
    latest_version = fetch_version_from_github()  # Replace with an actual versioning mechanism if needed

    # Compare stored version with the current version
    if CURRENT_VERSION != latest_version:
        print(f"A new version ({latest_version}) is available!")
        choice = input("Do you want to update? (y/n): ").strip().lower()
        if choice == "y":
            print("Updating...")

            # Perform the update here. This can be downloading a new executable, etc.
            download_executable()
            print("Download Complete. Installing...")
            hand_over(latest_version= latest_version)

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
        print(f"Version: {CURRENT_VERSION}")
        print("--- MAIN MENU ---")
        print("1. Enter Signups")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            signups_menu()
        elif choice == "0":
            c
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
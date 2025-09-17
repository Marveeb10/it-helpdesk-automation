"""
IT Help Desk Automation - Main Launcher
Author: Marvee Balyos

This script acts as the entry point for the IT Help Desk Automation toolkit.
It provides a simple menu to launch different utilities:
1. Reset Passwords
2. Batch Rename Files
3. Cleanup Temporary Files
4. Monitor System Resources
"""

import os
import subprocess
import sys

# Map menu options to their corresponding scripts
TOOLS = {
    "1": ("Reset Passwords", "reset_password.py"),
    "2": ("Batch Rename Files", "batch_rename.py"),
    "3": ("Cleanup Temporary Files", "cleanup_temp.py"),
    "4": ("Monitor System", "monitor_system.py"),
    "q": ("Quit", None),
}


def run_script(script_name: str):
    """Run another Python script in the same project folder."""
    try:
        subprocess.run([sys.executable, script_name], check=True)
    except FileNotFoundError:
        print(f"❌ Script {script_name} not found. Make sure it's in this folder.")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Error while running {script_name}: {e}")


def main():
    while True:
        print("\n=== IT Help Desk Automation Toolkit ===")
        for key, (desc, _) in TOOLS.items():
            print(f"[{key}] {desc}")

        choice = input("Select an option: ").strip().lower()

        if choice == "q":
            print("👋 Exiting Help Desk Toolkit. Goodbye!")
            break
        elif choice in TOOLS and TOOLS[choice][1]:
            print(f"\n🚀 Running {TOOLS[choice][0]}...\n")
            run_script(TOOLS[choice][1])
        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

"""
IT Help Desk Automation - Reset Password Script
Author: Marvee Balyos

This script simulates an IT Help Desk tool that:
- Loads user accounts from a CSV file
- Lets you reset ALL passwords or just ONE user’s password
- Generates strong random passwords
- Saves updated data into a new CSV
- Shows system memory usage at the end
"""

import pandas as pd
import psutil
import random
import string

CSV_FILE = "users.csv"


def generate_password(length: int = 10) -> str:
    """Generate a random secure password."""
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))


def reset_all_passwords(df: pd.DataFrame) -> pd.DataFrame:
    """Reset passwords for all users in the DataFrame."""
    df["Password"] = [generate_password() for _ in range(len(df))]
    return df


def reset_one_password(df: pd.DataFrame, username: str) -> pd.DataFrame:
    """Reset the password for a single user if they exist."""
    if username in df["Username"].values:
        new_pass = generate_password()
        df.loc[df["Username"] == username, "Password"] = new_pass
        print(f"✅ Password for '{username}' reset to: {new_pass}")
    else:
        print(f"❌ User '{username}' not found.")
    return df


def system_status():
    """Display system memory usage."""
    memory = psutil.virtual_memory()
    print(f"🖥️ System Memory Usage: {memory.percent}%")


if __name__ == "__main__":
    try:
        users_df = pd.read_csv(CSV_FILE)
        print(f"Loaded {len(users_df)} user accounts from {CSV_FILE}")
    except FileNotFoundError:
        print(f"❌ ERROR: Could not find {CSV_FILE}. Make sure it's in the same folder.")
        exit(1)

    print("\n🔐 Running Help Desk Password Reset Tool...")
    choice = input("Reset (A)ll users or (O)ne user? [A/O]: ").strip().lower()

    if choice == "a":
        users_df = reset_all_passwords(users_df)
        output_file = "users_updated.csv"
        users_df.to_csv(output_file, index=False)
        print(f"✅ All passwords reset. Saved to {output_file}")

    elif choice == "o":
        username = input("Enter username to reset: ").strip()
        users_df = reset_one_password(users_df, username)
        users_df.to_csv("users_updated.csv", index=False)

    else:
        print("⚠️ Invalid choice. Exiting.")

    # Show system status
    system_status()
    print("🚀 Done.")

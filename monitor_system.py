"""
monitor_system.py
Displays basic system performance metrics.
"""

import psutil


def monitor_system() -> None:
    """
    Print CPU, memory, and disk usage stats.

    Returns:
        None
    """
    print(f"🖥️ CPU Usage: {psutil.cpu_percent()}%")
    print(f"💾 Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"📂 Disk Usage: {psutil.disk_usage('/').percent}%")


if __name__ == "__main__":
    monitor_system()

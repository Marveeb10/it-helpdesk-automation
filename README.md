# IT Help Desk Automation Toolkit

This project simulates common IT Help Desk tasks using Python.  
It demonstrates automation skills relevant to technical support, IT operations, and system administration.  

The toolkit includes password resets, bulk file renaming, temporary file cleanup, and basic system monitoring — all built with Python, pandas, and psutil.  

---

## Features

- **Password Reset Tool**  
  Reads a CSV of user accounts (`users.csv`), generates secure random passwords, and writes updates to `users_updated.csv`.

- **Batch Rename Utility**  
  Renames groups of files in a target directory for faster file management.

- **Temporary File Cleanup**  
  Finds and deletes unnecessary temp/junk files to reclaim storage space.

- **System Monitoring**  
  Displays live system memory usage to simulate IT diagnostics.

---

## Project Structure
├── main.py # Main launcher with menu interface
├── reset_password.py # Password reset script
├── batch_rename.py # Bulk file renaming script
├── cleanup_temp.py # Temporary file cleanup script
├── monitor_system.py # System monitoring script
├── users.csv # Sample user accounts dataset
├── users_updated.csv # Updated users file (after reset)
├── requirements.txt # Dependencies
└── README.md # Project documentation

Technologies Used:
Python 3
pandas
psutil

## Notes

The included CSV files (users.csv, users_updated.csv) are sample datasets for demonstration.

In a real IT environment, these scripts could integrate with Active Directory, cloud APIs, or enterprise ticketing systems.

## Why This Project: 
I created this project to demonstrate how automation can make IT support more efficient. It reflects real-world help desk workflows and highlights my ability to:
Write clean, maintainable Python code
Automate repetitive technical tasks
Work with system resources and data files
Simulate IT operations in a safe, testable environment

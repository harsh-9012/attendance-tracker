# Attendance Tracker

## Project Overview
Attendance Tracker is a Python-based prototype that helps users manage attendance records for multiple subjects. It allows subjects to be added, attendance to be marked, percentages to be calculated, and records to be saved to a JSON file for later use.

This project demonstrates modular Python programming by separating logic into different files for subjects, attendance tracking, calculations, storage, logging, and report generation.

## Features
- Add subjects with a minimum attendance requirement
- Record attendance for each subject
- Calculate attendance percentage from present and total classes
- Save and load records using JSON storage
- Generate a simple text-based report in the console
- Log actions with timestamps

## Project Structure
- `main.py` - application entry point
- `subjects.py` - subject data and definitions
- `attendance.py` - attendance recording logic
- `calculator.py` - percentage calculation logic
- `storage.py` - JSON read/write operations
- `report.py` - console report generation
- `logger.py` - timestamped logging
- `attendance.json` - saved attendance data
- `attendance.log` - application logs

## Technologies Used
- Python 3
- JSON for simple data persistence
- VS Code
- Git and GitHub

## How to Run
1. Open a terminal in the project folder.
2. Run the project with:

```bash
python main.py
```

## Example Output
```text
Welcome to Attendance Tracker
Attendance for Math: 100.0%
Attendance Report:
Math: 100.00%
```

## Notes
This is a lightweight prototype and does not yet include advanced options such as subject editing/deletion, shortage calculations, chart-based reports, databases, or a graphical user interface. The current implementation is intended as a simple modular attendance tracker for learning and practice.

from subjects import Subjects
from attendance import Attendance
from calculator import Calculator
from report import Report
from storage import Storage
from logger import Logger

def main():
    print("Welcome to Attendance Tracker")

    subjects = Subjects()
    attendance = Attendance()
    calc = Calculator()
    report = Report()
    storage = Storage()
    logger = Logger()

    # Example flow
    subjects.add_subject("Math", 75)
    attendance.mark("Math", present=True)

    # Save data
    storage.save(attendance.records)
    logger.log("Attendance marked for Math")

    # Load data back
    data = storage.load()

    # Calculate percentage
    percent = calc.calculate(data["Math"], total_classes=data["Math"]["total"])
    print(f"Attendance for Math: {percent}%")

    # Generate report
    report.generate(data)

if __name__ == "__main__":
    main()

import datetime

class Logger:
    def __init__(self, filename="attendance.log"):
        self.filename = filename

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a") as f:
            f.write(f"[{timestamp}] {message}\n")

class Attendance:
    def __init__(self):
        self.records = {}

    def mark(self, subject, present=True):
        if subject not in self.records:
            self.records[subject] = {"present": 0, "total": 0}
        self.records[subject]["total"] += 1
        if present:
            self.records[subject]["present"] += 1

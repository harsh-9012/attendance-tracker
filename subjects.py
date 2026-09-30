class Subjects:
    def __init__(self):
        self.subjects = {}

    def add_subject(self, name, min_attendance):
        self.subjects[name] = {"min": min_attendance}

class Report:
    def generate(self, records):
        print("Attendance Report:")
        for subject, data in records.items():
            percent = (data["present"] / data["total"]) * 100 if data["total"] else 0
            print(f"{subject}: {percent:.2f}%")

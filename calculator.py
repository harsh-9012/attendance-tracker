class Calculator:
    def calculate(self, record, total_classes):
        if total_classes == 0:
            return 0
        return (record["present"] / total_classes) * 100

from statistics import median
from .base_report import BaseReport

class MedianCoffeeReport(BaseReport):
    def generate(self, records):
        data = {}
        for r in records:
            data.setdefault(r.student, []).append(r.coffee_spent)
        
        result = [(student, median(values)) for student, values in data.items()]
        
        result.sort(key=lambda x: x[1], reverse=True)
        return result
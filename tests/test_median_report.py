from statistics import median
import pytest
from coffee_report.models import Record
from coffee_report.reports.median_coffee import MedianCoffeeReport

@pytest.fixture
def sample_records():
    return [
        Record("Alice", "2024-06-01", 100, 7.0, 5, "good", "Math"),
        Record("Alice", "2024-06-02", 150, 6.5, 6, "ok", "Math"),
        Record("Bob", "2024-06-01", 200, 6.0, 4, "tired", "Math"),
        Record("Bob", "2024-06-02", 300, 5.5, 5, "ok", "Math"),
        Record("Charlie", "2024-06-01", 50, 8.0, 3, "good", "Math"),
    ]

def test_median_calculation(sample_records):
    report = MedianCoffeeReport()
    result = report.generate(sample_records)

    # Проверяем медианы
    medians = dict(result)
    assert medians["Alice"] == median([100, 150])
    assert medians["Bob"] == median([200, 300])
    assert medians["Charlie"] == 50

def test_sorting_desc(sample_records):
    report = MedianCoffeeReport()
    result = report.generate(sample_records)

    sorted_medians = [value for _, value in result]
    assert sorted_medians == sorted(sorted_medians, reverse=True)

def test_empty_records():
    report = MedianCoffeeReport()
    result = report.generate([])
    assert result == []
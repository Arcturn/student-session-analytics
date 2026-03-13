import pytest
from pathlib import Path
from coffee_report.reader import read_files
from coffee_report.models import Record

TEST_CSV_CONTENT = """student,date,coffee_spent,sleep_hours,study_hours,mood,exam
Alice,2024-06-01,100,7,5,good,Math
Bob,2024-06-01,200,6,4,tired,Math
Alice,2024-06-02,150,6.5,6,ok,Math
"""

@pytest.fixture
def tmp_csv_file(tmp_path):
    file = tmp_path / "test.csv"
    file.write_text(TEST_CSV_CONTENT, encoding="utf-8")
    return str(file)

def test_read_files_single(tmp_csv_file):
    records = read_files([tmp_csv_file])
    assert len(records) == 3
    assert isinstance(records[0], Record)
    assert records[0].student == "Alice"
    assert records[0].coffee_spent == 100
    assert records[1].student == "Bob"

def test_read_files_missing_file():
    with pytest.raises(FileNotFoundError):
        read_files(["non_existent.csv"])

def test_read_files_multiple(tmp_path):
    file1 = tmp_path / "f1.csv"
    file1.write_text(TEST_CSV_CONTENT, encoding="utf-8")
    file2 = tmp_path / "f2.csv"
    file2.write_text(TEST_CSV_CONTENT, encoding="utf-8")

    records = read_files([str(file1), str(file2)])
    assert len(records) == 6  # 3 + 3 строки
    students = [r.student for r in records]
    assert students.count("Alice") == 4
    assert students.count("Bob") == 2
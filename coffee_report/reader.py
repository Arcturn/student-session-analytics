import csv
from pathlib import Path

from .models import Record


def read_files(files: list[str]) -> list[Record]:
    records: list[Record] = []

    for file_path in files:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        with path.open(encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                records.append(
                    Record(
                        student=row["student"],
                        date=row["date"],
                        coffee_spent=int(row["coffee_spent"]),
                        sleep_hours=float(row["sleep_hours"]),
                        study_hours=int(row["study_hours"]),
                        mood=row["mood"],
                        exam=row["exam"],
                    )
                )

    return records
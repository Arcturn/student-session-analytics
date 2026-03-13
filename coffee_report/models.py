from dataclasses import dataclass


@dataclass
class Record:
    student: str
    date: str
    coffee_spent: int
    sleep_hours: float
    study_hours: int
    mood: str
    exam: str
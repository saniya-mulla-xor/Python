import csv
import math
import os
import tempfile
from pathlib import Path
from statistics import mean, median

from .models import Student


def format_score(score):
    return f"{score:g}"


class GradeBook:
    def __init__(self):
        self.students = {}
        self.subjects = []
        self.warnings = []

    @classmethod
    def load(cls, path):
        gradebook = cls()
        with Path(path).open(newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for line_number, row in enumerate(reader, start=2):
                name = (row.get("student") or "").strip()
                subject = (row.get("subject") or "").strip()
                raw_score = row.get("score")

                try:
                    score = float(raw_score)
                    if not math.isfinite(score) or not 0 <= score <= 100:
                        raise ValueError
                except (TypeError, ValueError):
                    gradebook.warnings.append(
                        f"Warning: line {line_number}: skipped bad score "
                        f"'{raw_score or ''}' for {name}"
                    )
                    continue

                if not name or not subject:
                    gradebook.warnings.append(
                        f"Warning: line {line_number}: skipped row with "
                        "missing student or subject"
                    )
                    continue

                student = gradebook.students.setdefault(name, Student(name))
                if subject not in gradebook.subjects:
                    gradebook.subjects.append(subject)
                student.scores[subject] = score

        return gradebook

    def ranked_students(self):
        return sorted(
            self.students.values(),
            key=lambda student: (-student.average(), student.name),
        )

    def get_student(self, name):
        return self.students.get(name)

    def add_score(self, name, subject, score):
        if not math.isfinite(score) or not 0 <= score <= 100:
            raise ValueError(f"score must be 0-100, got {score}")
        if not name.strip() or not subject.strip():
            raise ValueError("student and subject must not be empty")

        student = self.students.setdefault(name, Student(name))
        if subject not in self.subjects:
            self.subjects.append(subject)
        student.scores[subject] = score

    def subject_statistics(self, subject):
        scores = [
            student.scores[subject]
            for student in self.students.values()
            if subject in student.scores
        ]
        if not scores:
            return None
        return mean(scores), median(scores), min(scores), max(scores), len(scores)

    def save(self, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary_path = None

        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                newline="",
                encoding="utf-8",
                dir=path.parent,
                delete=False,
            ) as file:
                temporary_path = Path(file.name)
                writer = csv.writer(file)
                writer.writerow(("student", "subject", "score"))
                for student in self.students.values():
                    for subject in self.subjects:
                        if subject in student.scores:
                            writer.writerow(
                                (student.name, subject, format_score(student.scores[subject]))
                            )
            os.replace(temporary_path, path)
        finally:
            if temporary_path is not None and temporary_path.exists():
                temporary_path.unlink()

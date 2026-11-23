import argparse

from .gradebook import GradeBook, format_score
from .models import letter_grade


def _print_report(gradebook):
    subjects = gradebook.subjects
    header_widths = {"English": 12, "Math": 6, "Physics": 11}
    print(
        f"{'Student':<10}"
        + "".join(
            f"{subject:<{header_widths.get(subject, len(subject) + 2)}}"
            for subject in subjects
        )
        + f"{'Avg':<5}Grade"
    )
    print("-" * 49)

    for student in gradebook.ranked_students():
        scores = "".join(
            f"{format_score(student.scores[subject]) if subject in student.scores else '-':>9}"
            for subject in subjects
        )
        print(
            f"{student.name:<8}{scores}{student.average():>7.1f}  "
            f"{letter_grade(student.average())}"
        )

    print()
    for subject in subjects:
        stats = gradebook.subject_statistics(subject)
        subject_mean, subject_median, minimum, maximum, count = stats
        print(
            f"{subject}: mean {subject_mean:.1f}, median {format_score(subject_median)}, "
            f"range {format_score(minimum)}-{format_score(maximum)} ({count} scores)"
        )

    below_60 = [
        student.name
        for student in gradebook.ranked_students()
        if student.average() < 60
    ]
    print(f"Below 60 average: {', '.join(below_60)}")


def _print_student(gradebook, name):
    student = gradebook.get_student(name)
    if student is None:
        print(f"Error: no student named {name}")
        return 1

    for subject in gradebook.subjects:
        score = (
            format_score(student.scores[subject])
            if subject in student.scores
            else "-"
        )
        print(f"  {subject:<9}{score:>5}")
    print(f"  average {student.average():.1f} -> {letter_grade(student.average())}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="View and update student grades.")
    parser.add_argument("--file", default="../data/grades.csv", help="CSV grade file")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("report", help="show the full grade report")
    student_parser = commands.add_parser("student", help="show one student's grades")
    student_parser.add_argument("name")
    top_parser = commands.add_parser("top", help="show the top students")
    top_parser.add_argument("count", type=int)
    add_parser = commands.add_parser("add", help="add or update a score")
    add_parser.add_argument("name")
    add_parser.add_argument("subject")
    add_parser.add_argument("score", type=float)

    args = parser.parse_args(argv)
    try:
        gradebook = GradeBook.load(args.file)
    except FileNotFoundError as error:
        print(f"Error: {error}")
        return 1

    for warning in gradebook.warnings:
        print(warning)

    if args.command == "report":
        _print_report(gradebook)
    elif args.command == "student":
        return _print_student(gradebook, args.name)
    elif args.command == "top":
        if args.count < 0:
            print("Error: N must be non-negative")
            return 1
        for rank, student in enumerate(gradebook.ranked_students()[: args.count], start=1):
            print(f"{rank}. {student.name} {student.average():.1f}")
    else:
        try:
            gradebook.add_score(args.name, args.subject, args.score)
        except ValueError as error:
            print(f"Error: {error}")
            return 1
        gradebook.save(args.file)
        print(
            f"Added {args.name} {args.subject}: "
            f"{format_score(args.score)}"
        )
    return 0

from pathlib import Path


def parse_readings(lines):
    values = []
    bad = []

    for line_number, line in enumerate(lines, start=1):
        text = line.strip()
        try:
            values.append(float(text))
        except ValueError:
            bad.append((line_number, text))

    return values, bad


path = Path(__file__).resolve().parent / "data" / "readings.txt"
lines = path.read_text(encoding="utf-8").splitlines()
values, bad = parse_readings(lines)

print(f"Lines: {len(lines)}")
print(f"Valid: {len(values)}")
print(f"Invalid lines: {[line_number for line_number, _ in bad]}")
for line_number, text in bad:
    print(f"  line {line_number}: {text!r}")

if values:
    average = sum(values) / len(values)
    print(f"Average: {average:.2f}")
    print(f"Min: {min(values):g}  Max: {max(values):g}")
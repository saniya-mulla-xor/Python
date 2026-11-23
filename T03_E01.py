from pathlib import Path


def file_stats(path):
    stats = {"lines": 0, "words": 0, "characters": 0, "blank": 0}

    with open(path, encoding="utf-8") as file:
        for line in file:
            text = line.rstrip("\r\n")
            stats["lines"] += 1
            stats["words"] += len(text.split())
            stats["characters"] += len(text)
            if not text.strip():
                stats["blank"] += 1

    return stats


path = Path(__file__).resolve().parent / "data" / "notes.txt"

with open(path, encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        if line_number > 5:
            break
        text = line.rstrip("\r\n")
        print(f"{line_number:3}: {text}")

stats = file_stats(path)
print(f"Lines: {stats['lines']}")
print(f"Words: {stats['words']}")
print(f"Characters: {stats['characters']}")
print(f"Blank lines: {stats['blank']}")
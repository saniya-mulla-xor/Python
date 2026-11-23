from pathlib import Path


def write_squares(path, n):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        for i in range(1, n + 1):
            file.write(f"{i} squared is {i * i}\n")

    return n


output_path = Path(__file__).resolve().parent / "output" / "squares.txt"
lines_written = write_squares(output_path, 8)
print(f"Lines written: {lines_written}")
print(output_path.read_text(encoding="utf-8"), end="")
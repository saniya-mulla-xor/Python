# Python Exercises

This folder contains standalone Python exercise solutions (`T01_E01.py` through
`T13_E02.py`), sample input data, and the two multi-module command-line projects
for T13. The prompts shared for T07 through T13 are documented in
[QUESTIONS.md](QUESTIONS.md).

## Requirements

- Python 3.7 or newer
- No third-party packages are required

Run standalone exercises from this folder, for example:

```powershell
python T07_E01.py
```

## T13 command-line projects

The root-level `T13_E01.py` and `T13_E02.py` files are launchers for the
packages in `solutions/`.

Run the to-do manager from the exercise folder:

```powershell
python T13_E01.py --file todo.json
```

Run the grade manager and its subcommands:

```powershell
python T13_E02.py --file data\grades.csv report
python T13_E02.py --file data\grades.csv student Ana
python T13_E02.py --file data\grades.csv top 3
python T13_E02.py --file data\grades.csv add Chloe Physics 95
```

The grade manager requires a subcommand: `report`, `student`, `top`, or `add`.
The sample grade data is in `data/grades.csv`.

The packages can also be run directly from `solutions/`:

```powershell
cd solutions
python -m t13_e01_todo --file ..\todo.json
python -m t13_e02_grades --file ..\data\grades.csv report
```

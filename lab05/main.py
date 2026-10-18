from pathlib import Path
from tablestats import read_rows, count_types, total_minutes, to_csv

def main(): filename = 'events-small'
with open(path, encoding="utf-8") as table:
    rows = read_rows(table)
counts = count_types(rows)
print(len(rows))
print(len(counts))
print(f"{total_minutes(rows, 'ошибка'):.1f}")
summary_path = Path(__file__).resolve().parent / "summary.csv"
path=input().strip()
with open(summary_path, "w", encoding="utf-8") as out:
    out.write(to_csv(counts))

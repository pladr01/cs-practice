from tablestats import read_rows, count_types, total_minutes, to_csv

with open("tablestats.py", 'r', encoding="utf-8") as table:
    rows = read_rows(table.readlines())
    print(len(rows))
    print(len(count_types(rows)))
    print(total_minutes(rows, 'ошибка'))

with open("summary.csv", "w", encoding="utf-8") as outcome:
    counts = count_types(rows)
    outcome.write(to_csv(counts))

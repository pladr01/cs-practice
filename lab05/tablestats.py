def read_rows(lines):
    rows = []
    header = None
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        fields = []
        for value in line.split(","):
            fields.append(value.strip())
        if header is None:
            header = fields
            continue
        if len(fields) != len(header):
            continue
        row = {}
        for i in range(len(header)):
            row[header[i]] = fields[i]
        rows.append(row)
    return rows


def count_types(rows):
    counts = {}
    for row in rows:
        kind = row["тип"]
        if kind not in counts:
            counts[kind] = 0
        counts[kind] += 1
    return counts


def total_minutes(rows, kind):
    total = 0.0
    for row in rows:
        if row["тип"] != kind:
            continue
        value = row["минуты"].replace(",", ".")
        try:
            minutes = float(value)
        except ValueError:
            continue
        total += minutes
    return round(total, 1)
def to_csv(counts):
    text = "тип,количество\n"
    for kind in sorted(counts):
        text += f"{kind},{counts[kind]}\n"
    return text
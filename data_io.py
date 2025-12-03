import csv
def read_points_from_console():
    raw_x = input("Introduceți valorile lui x (separate prin spațiu sau virgulă): ")
    raw_y = input("Introduceți valorile lui y (separate prin spațiu sau virgulă): ")

    def parse_line(line):
        separators = [',', ' ']
        for sep in separators:
            if sep in line:
                parts = [p for p in line.replace(',', ' ').split() if p]
                break
        else:
            parts = [line]
        values = []
        for p in parts:
            try:
                values.append(float(p))
            except ValueError:
                raise ValueError(f"Valoare invalidă detectată: {p}")
        return values

    x_values = parse_line(raw_x)
    y_values = parse_line(raw_y)

    if len(x_values) != len(y_values):
        raise ValueError("Numărul de valori x nu este egal cu numărul de valori y.")
    if len(x_values) < 2:
        raise ValueError("Sunt necesare cel puțin 2 puncte pentru regresie.")

    return x_values, y_values

def read_points_from_csv(path):
    x_values = []
    y_values = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row_index, row in enumerate(reader, start=1):
            if len(row) < 2:
                print(f"Linia {row_index} ignorată: nu are cel puțin 2 coloane.")
                continue
            try:
                x = float(row[0])
                y = float(row[1])
                x_values.append(x)
                y_values.append(y)
            except ValueError:
                print(f"Linia {row_index} ignorată: date nenumerice ({row}).")
                continue

    if len(x_values) != len(y_values) or len(x_values) < 2:
        raise ValueError("Fișierul nu conține suficiente puncte valide sau datele sunt inconsistente.")
    return x_values, y_values


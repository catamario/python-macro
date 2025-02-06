import re


def extract_coordinates(file_path, start_line=27825, end_line=29863):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    selected_lines = lines[start_line - 1:end_line]  # Ajustare pentru indexare de la 0
    pattern = re.compile(
        r"MoveMouseRelative\(\s*(-?\d+)\s*(?:\*\s*multiplier)?\s*,\s*(-?\d+)\s*(?:\*\s*multiplier)?\s*\)")

    coordinates = []
    for line in selected_lines:
        for match in pattern.finditer(line):
            x, y = int(match.group(1)), int(match.group(2))
            coordinates.append((x, y))

    return coordinates

# Exemplu de utilizare:
file_path = "FULL_PACK_MACRO_[unknowncheats.me]_.lua"
coords = extract_coordinates(file_path) #2467 la 4573
print(coords)

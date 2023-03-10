import re

def convert(string: str):
    if string.isdigit():
        return int(string)
    elif string.replace('.', '').isdigit():
        return float(string)

    return string

def parse(csv: str, sep=r'\s*,\s*', newline_char=r'\n') -> list[list]:
    i: int
    j: str
    item: str

    lines: list[str] = re.split(newline_char, csv)
    
    for i, j in enumerate(lines):
        lines[i] = [convert(item) for item in re.split(sep, j)]

    return lines

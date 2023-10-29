def load_map(filename: str):
    with open(filename) as f:
        lines = f.readlines()
    return lines

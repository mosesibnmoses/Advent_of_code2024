def parse_input(file_path,whole=False):
    """Read a file and return a list of stripped lines."""
    with open(file_path, 'r') as f:
        if whole:
            return f.read()
        return [line.strip() for line in f]

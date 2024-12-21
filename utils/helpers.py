def parse_input(file_path):
    """Read a file and return a list of stripped lines."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]
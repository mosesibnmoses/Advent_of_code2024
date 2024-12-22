import numpy as np

def parse_input(file_path,whole=False):
    """Read a file and return a list of stripped lines."""
    with open(file_path, 'r') as f:
        if whole:
            return f.read()
        return [line.strip() for line in f]

def read_grid(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        num_lines = len(lines)
        flat_data = ''.join(lines)
        grid = np.array(list(flat_data), dtype='U1')  # 'U1' for single Unicode characters
        return grid.reshape(num_lines, -1)


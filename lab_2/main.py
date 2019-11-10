"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
    def generate_edit_matrix(num_rows: int, num_cols: int) -> list:
        matrix = []
        row = []
        for i in range(num_cols):
            row.append(0)
        for j in range(num_rows):
            matrix.append(row.copy())

    pass


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    pass


def minimum_value(numbers: tuple) -> int:
    pass


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:
    pass


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:
    pass

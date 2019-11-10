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

    return matrix

    pass


def initialize_edit_matrix(edit_matrix: tuple, add_weight: int, remove_weight: int) -> list:
    edit_matrix = list(edit_matrix)

    if len(edit_matrix) == 0 or len(edit_matrix[0]) == 0 or not add_weight or not remove_weight:
        return edit_matrix

    for i in range(1, len(edit_matrix)):
        edit_matrix[i][0] = edit_matrix[i - 1][0] + remove_weight

    for j in range(1, len(edit_matrix[0])):
        edit_matrix[0][j] = edit_matrix[0][j - 1] + add_weight
    print(edit_matrix)

    return edit_matrix

    initialize_edit_matrix(([0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]), 1, 1)
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

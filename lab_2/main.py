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

    return edit_matrix
    pass


def minimum_value(numbers: tuple) -> int:
    minimum = numbers[0]
    for elem in numbers:
        if elem < minimum:
            minimum = elem

    # minimum = min(numbers)

    return minimum

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
    edit_matrix = list(edit_matrix)
    if not original_word or not target_word or type(add_weight) != int or type(remove_weight) != int \
            or type(substitute_weight) != int:
        return edit_matrix
    for i in range(1, len(edit_matrix)):
        for j in range(1, len(edit_matrix[0])):
            if original_word[i - 1] != target_word[j - 1]:
            s_w = substitute_weight
    else:
        s_w = 0
    edit_matrix[i][j] = minimum_value((edit_matrix[i - 1][j] + remove_weight,
                                       edit_matrix[i][j - 1] + add_weight,
                                       edit_matrix[i - 1][j - 1] + s_w))
    return edit_matrix
    pass

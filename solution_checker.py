import numpy as np


def valid_solution(board):
    """
    Board is a 9x9 nested Python list
    """
    expected = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    board = np.array(board)
    for i in range(9):
        test = board[i, :]
        if set(test.flatten()) != expected:
            return False
        test = board[:, i]
        if set(test.flatten()) != expected:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            test = board[i : i + 3, j : j + 3]
            if set(test.flatten()) != expected:
                return False

    return True

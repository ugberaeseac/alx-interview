#!/usr/bin/python3
"""
N queens puzzle - challenge of placing N non-attacking
queens on an N×N chessboard
Only allowed to import the sys module
N must be an integer greater or equal to 4
print the possible solutions
"""


import sys


def nqueens(N):
    """
    solve nqueen problem
    """
    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    chess_board = [[0] * N for _ in range(N)]
    if not place_queen(chess_board, 0, N):
        sys.exit(1)


def place_queen(chess_board, row, N):
    """
    places a queen on the chessboard
    """
    if row == N:
        print_solution(chess_board)
        return True

    result = False
    for col in range(N):
        if check_ifsafe(chess_board, row, col, N):
            chess_board[row][col] = 1
            result = place_queen(chess_board, row + 1, N) or result
            chess_board[row][col] = 0

    return result


def check_ifsafe(chess_board, row, col, N):
    """
    check if its safe to place a queen
    at a given position
    """
    for i in range(row):
        if chess_board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if chess_board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if chess_board[i][j] == 1:
            return False

    return True


def print_solution(chess_board):
    """
    print possible solutions
    """
    solution = []
    for i in range(len(chess_board)):
        for j in range(len(chess_board[i])):
            if chess_board[i][j] == 1:
                solution.append([i, j])
    print(solution)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    nqueens(N)

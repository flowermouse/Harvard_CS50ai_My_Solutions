"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    elif terminal(board):
        return 'Game Over'
    else:
        if sum([board[i].count(X) for i in range(3)]) > sum([board[i].count(O) for i in range(3)]):
            return O
        else:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return 'Game Over'
    else:
        available = set()
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    available.add((i, j))
        return available


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if i < 0 or j < 0:
        raise ValueError('invalid action')
    if terminal(board) or board[i][j] != EMPTY:
        raise NameError('invalid action')
    else:
        p = player(board)
        new = deepcopy(board)
        new[i][j] = p
        return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
        
    transposed = list(zip(*board))  # unpacking and packing
    for row in transposed:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
    
    if all([board[i][i] == X for i in range(3)]) or all([board[i][2 - i] == X for i in range(3)]):
        return X
    elif all([board[i][i] == O for i in range(3)]) or all([board[i][2 - i] == O for i in range(3)]):
        return O
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def MaxValue(board):
        if terminal(board):
            return utility(board), None
        else:
            value = - float('inf')
            best = None
            for action in actions(board):
                if MinValue(result(board, action))[0] > value:
                    value = MinValue(result(board, action))[0]
                    best = action
            return value, best

    def MinValue(board):
        if terminal(board):
            return utility(board), None
        else:
            value = float('inf')
            best = None
            for action in actions(board):
                if MaxValue(result(board, action))[0] < value:
                    value = MaxValue(result(board, action))[0]
                    best = action 
            return value, best
   
    if terminal(board):
        return None
    else:
        if player(board) == X:
            return MaxValue(board)[1]
        else:
            return MinValue(board)[1]

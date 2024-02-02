def get_neighbor_count(board, row, col):
    """ Compte les voisins vivants d'une cellule. """
    rows, cols = len(board), len(board[0])
    count = 0

    for i in range(max(0, row - 1), min(row + 2, rows)):
        for j in range(max(0, col - 1), min(col + 2, cols)):
            if (i, j) != (row, col) and board[i][j]:
                count += 1

    return count

def next_board_state(board):
    """ Calcule l'état suivant du jeu de la vie. """
    rows, cols = len(board), len(board[0])
    next_board = [[False for _ in range(cols)] for _ in range(rows)]

    for row in range(rows):
        for col in range(cols):
            neighbors = get_neighbor_count(board, row, col)
            if board[row][col]:  # Cellule vivante
                next_board[row][col] = neighbors in [2, 3]
            else:  # Cellule morte
                next_board[row][col] = neighbors == 3

    return next_board

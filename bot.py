import time
import logging

logging.basicConfig(level=logging.WARNING)

ct = 1
def solve(board, match, colours, seq):   
    global ct
    gridSize = len(match[0])
    if complete(board, match, seq, gridSize):
        return True
    logging.debug('Solve Called: ' + str(ct))
    ct += 1
    for colour in colours:
        for i in range(gridSize*2):
            if valid(match, i, colour, seq):
                group = (i,colour)
                seq.append(group)
                newboard = makeMove(board, i, colour)
                # time.sleep(1)
                if solve(newboard, match, colours, seq):
                    return seq
                seq.remove(group)
                newboard = board

def complete(board, match, seq, gridSize):
    if board == match and len(seq) == gridSize * 2:  # sequence found
        return True
    else:
        for x in range(len(match)):
            for i in range(len(match)):
                if match[x][i] != board[x][i]:
                    if match[x][i] == '-':
                        pass
                    else:
                        return False

        if len(seq) == gridSize * 2:
            return True
        return False

def makeMove(board, move, colour):
    # Finds axis and inserts colour
    gridSize = len(board[0])
    if move >= gridSize:
        move -= gridSize
        for i in range(gridSize):
            board[i][move] = colour
    else:
        for i in range(gridSize):
            board[move][i] = colour
    return board

def valid(match, move, choice, seq):
    for i in range(len(seq)):               # Button already pressed
        if move == seq[i][0]:
            return False
    return True
    # gridSize = len(match[0])
    # # if move > gridSize*2 or move < 0:     # Out of Range
    # #     print('Choice out of range')
    # #     return False
    # if move >= gridSize:                    # Vertical
    #     move -= gridSize
    #     for i in range(gridSize):
    #         if match[i][move] == '-':
    #             return True
    #         return choice == match[i][move]
    # else:                                   # Horizontal
    #     for i in range(gridSize):
    #         if choice != match[move][i]:
    #             if match[move][i] == '-':
    #                 return True
    #         return choice == match[move][i]

def printBoard(board):
    gridSize = len(board[0])
    print('\n')
    for i in range(gridSize):
        for j in range(len(board[i])):
            if j == gridSize:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end='')
        print('')
    print('\n')


inb = [['-', '-'], ['-', '-']]
mat = [['W', 'O'], ['-', 'B']]
col = ['W', 'O', 'B']
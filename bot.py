"""
Full Grid:
[
[['-', '-', '-'], ['-', '-', 'P']],
[['-', '-', 'P'], ['-', '-', '-']],
]
"""
colours = ['P']
inboard = [
    [['-'], ['P']],
    [['P'], ['-']]
]
xboard = [
    [['-'], ['P'], ['P']],
    [['P'], ['-'], ['P']],
    [['P'], ['-'], ['P']]
]

def solve(bo):
    seq = []
    if len(bo[0][0][:]) != 3:
        bo = convert_board(bo)
    pos = find_empty(bo)
    if not pos:
        return True
    row,col,num = pos
    # Function to get colours goes here
    for colour in colours:
        if valid(colour, pos, bo):
            if num == 2:
                bo[row][col][1] == colour
                if solve(bo):
                    return True
                # bo[row][col][1] == '-'
            else:
                bo[row][col][0] == colour
                if solve(bo):
                    return True
                bo[row][col][0] == '-'

            # Might need to replace bottom colour as well.
            # bo[row][col][0] == '-'

    return False
    

def valid(choice, pos, bo):
    row,col,num = pos
    if num == 1:
        # choice not match bottom colour
        if choice != bo[row][col][2]:
            # bottom colour is None
            if bo[row][col][2] == '-':
                return True
            return False
    return True
    
def convert_board(bo):
    newbo = []
    for x in range(len(bo)):
        row = []
        for y in range(len(bo[x])):
            row.append(['-','-',bo[x][y][0]])
        newbo.append(row)
    return newbo

def print_board(bo):
    # rows =    bo[0]
    # choices = bo[0][0]
    # letters = bo[0][0][0]
    if len(bo[0][0][:]) != 3:
        bo = convert_board(bo)
    gs = len(bo[0])
    print('\n')
    for i in range(len(bo[0])):
        for j in range(len(bo[i])):
            if j == gs:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end='')
        print('')
    print('\n')

def find_empty(bo):
    for row in range(len(bo[0])):
        for col in range(len(bo[row])):
            if bo[row][col][0] == '-':
                if bo[row][col][1] == '-':
                    return (row,col,2)
                return (row,col,1)


x = [[['P', 'P', 'P'], ['P', 'P', 'P']], [['P', 'P', 'P'], ['X', '-', '-']]]
y = [[['X', '-', '-'], ['X', '-', 'P'], ['X', '-', 'P']], [['-', 'X', 'P'], ['X', '-', '-'], ['X', '-', 'P']], [['-', '-', 'P'], ['-', '-', '-'], ['-', '-', 'P']]]


print_board(inboard)
solve(inboard)
print('--------------')
print_board(inboard)

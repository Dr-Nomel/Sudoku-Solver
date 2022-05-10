import math

inpuut = [
    ['.', '.', '.', '3', '.', '.', '.', '.', '.'],
    ['8', '.', '.', '.', '.', '.', '.', '.', '6'],
    ['.', '.', '5', '.', '1', '9', '4', '.', '.'],
    ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
    ['.', '.', '1', '.', '7', '5', '9', '.', '.'],
    ['.', '9', '.', '.', '.', '.', '.', '4', '.'],
    ['.', '.', '.', '2', '.', '.', '7', '.', '.'],
    ['.', '.', '3', '4', '.', '.', '.', '.', '.'],
    ['5', '.', '.', '.', '3', '7', '.', '8', '.'],
]

def clean(str):
    ans = ''
    for i in range(len(str)):
        if str[i] != ' ':
            ans += str[i]
    return ans

def solve_sudoku(board):
    size = 9
    box_size = 3


    def find_empty(board):

        for r in range(size):
            for c in range(size):

                if not board[r][c] in '123456789':
                    return [r,c]
        return None

    def validate(num, pos, board):
        [r,c] = pos

        for i in range(size):
            if board[i][c] == num and i != r:
                return False

        for i in range(size):
            if board[r][i] == num and i != c:
                return False

        box_row = math.floor(r/box_size) * box_size
        box_col = math.floor(c/box_size) * box_size

        for i in range(box_row, box_row + box_size):
            for j in range(box_col, box_col + box_size):
                if board[i][j] == num and i != r and j != c:
                    return False

        return True

    def solve():
        cur_pos = find_empty(board)
        if(cur_pos == None):
            return True

        for i in range(1, size+1):
            cur_num = str(i)
            is_valid = validate(cur_num,cur_pos, board)

            if is_valid:
                [x,y] = cur_pos
                board[x][y] = cur_num

                if solve():
                    return True

                board[x][y] = '.'
        return False

    solve()


nums_1 = []
s_1 = clean(input())
for i in range(len(s_1)):
    nums_1.append(s_1[i])

nums_2 = []
s_2 = clean(input())
for i in range(len(s_2)):
    nums_2.append(s_2[i])

nums_3 = []
s_3 = clean(input())
for i in range(len(s_3)):
    nums_3.append(s_3[i])

nums_4 = []
s_4 = clean(input())
for i in range(len(s_4)):
    nums_4.append(s_4[i])

nums_5 = []
s_5 = clean(input())
for i in range(len(s_5)):
    nums_5.append(s_5[i])

nums_6 = []
s_6 = clean(input())
for i in range(len(s_6)):
    nums_6.append(s_6[i])

nums_7 = []
s_7 = clean(input())
for i in range(len(s_7)):
    nums_7.append(s_7[i])

nums_8 = []
s_8 = clean(input())
for i in range(len(s_8)):
    nums_8.append(s_8[i])

nums_9 = []
s_9 = clean(input())
for i in range(len(s_9)):
    nums_9.append(s_9[i])

for i in range(9):
    inpuut[0][i] = nums_1[i]

for i in range(9):
    inpuut[1][i] = nums_2[i]

for i in range(9):
    inpuut[2][i] = nums_3[i]

for i in range(9):
    inpuut[3][i] = nums_4[i]

for i in range(9):
    inpuut[4][i] = nums_5[i]

for i in range(9):
    inpuut[5][i] = nums_6[i]

for i in range(9):
    inpuut[6][i] = nums_7[i]

for i in range(9):
    inpuut[7][i] = nums_8[i]

for i in range(9):
    inpuut[8][i] = nums_9[i]
proof = inpuut
solve_sudoku(inpuut)
if(proof == inpuut):
    print("Решение : ")
    for i in range(9):
        print(*inpuut[i], sep = '  ')
else:
    print("Нет решения")
import math

inpuut = [
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '9', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
]

def clean(str):
    ans = ''
    for i in range(len(str)):
        if  str[i] in '0123456789':
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

for i in range(9):
    inpuut[i] = [c for c in clean(input())]
proof = inpuut
solve_sudoku(inpuut)
if(proof == inpuut):
    print("Решение : ")
    for i in range(9):
        print(*inpuut[i], sep = '  ')
else:
    print("Нет решения")


# Easy :
# 8 0 1 0 0 7 0 6 4
# 0 0 0 0 1 3 0 8 2
# 6 7 2 9 0 4 0 0 0
# 0 1 5 0 7 0 0 9 0
# 0 0 3 4 2 0 0 1 0
# 0 0 8 0 0 1 0 0 0
# 0 0 0 0 3 0 6 0 0
# 3 9 6 0 0 5 0 2 1
# 0 8 4 1 9 6 0 0 5


# Ans :
#8  3  1  2  5  7  9  6  4
#5  4  9  6  1  3  7  8  2
#6  7  2  9  8  4  1  5  3
#4  1  5  3  7  8  2  9  6
#7  6  3  4  2  9  5  1  8
#9  2  8  5  6  1  4  3  7
#1  5  7  8  3  2  6  4  9
#3  9  6  7  4  5  8  2  1
#2  8  4  1  9  6  3  7  5


# Medium :
# 9 8 4 0 0 0 0 0 1
# 0 5 0 8 0 0 6 4 0
# 6 0 0 0 0 9 0 2 0
# 0 0 0 7 6 0 0 0 5
# 0 7 0 4 0 0 9 0 0
# 0 0 0 0 0 0 3 0 0
# 0 3 0 0 0 7 0 9 6
# 0 4 5 0 9 0 0 0 8
# 0 0 0 2 0 0 7 5 3


# Ans :
# 9  8  4  6  7  2  5  3  1
# 2  5  7  8  3  1  6  4  9
# 6  1  3  5  4  9  8  2  7
# 4  2  9  7  6  3  1  8  5
# 3  7  8  4  1  5  9  6  2
# 5  6  1  9  2  8  3  7  4
# 8  3  2  1  5  7  4  9  6
# 7  4  5  3  9  6  2  1  8
# 1  9  6  2  8  4  7  5  3


# Hard :
# 0 0 8 0 9 0 4 0 0
# 3 0 2 7 6 0 0 0 0
# 1 0 0 0 2 0 0 0 8
# 6 0 0 0 0 0 0 2 0
# 0 0 0 0 1 0 0 0 0
# 2 0 0 8 0 3 0 0 0
# 0 0 0 5 0 0 8 0 7
# 0 0 0 6 0 0 0 0 4
# 0 7 0 0 8 9 0 0 5


# Ans :
# 5  6  8  3  9  1  4  7  2
# 3  4  2  7  6  8  9  5  1
# 1  9  7  4  2  5  6  3  8
# 6  8  5  9  4  7  1  2  3
# 7  3  4  2  1  6  5  8  9
# 2  1  9  8  5  3  7  4  6
# 9  2  6  5  3  4  8  1  7
# 8  5  1  6  7  2  3  9  4
# 4  7  3  1  8  9  2  6  5


#Expert :
# 5 0 0 0 7 0 0 8 4
# 0 0 9 0 0 1 2 0 0
# 0 0 0 5 0 9 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 1 0 0 9 6 0 4 0
# 7 5 3 0 0 0 1 0 0
# 0 7 4 0 0 0 0 0 0
# 0 0 0 0 0 3 0 2 0
# 9 0 0 0 0 0 3 0 0


# Ans :
# 5  3  1  6  7  2  9  8  4
# 6  4  9  8  3  1  2  5  7
# 8  2  7  5  4  9  6  1  3
# 4  9  6  1  5  7  8  3  2
# 2  1  8  3  9  6  7  4  5
# 7  5  3  2  8  4  1  9  6
# 3  7  4  9  2  8  5  6  1
# 1  8  5  7  6  3  4  2  9
# 9  6  2  4  1  5  3  7  8


# Evil :
# 0 0 5 0 0 0 0 2 0
# 9 0 0 4 0 0 1 0 5
# 0 0 0 0 1 0 0 7 0
# 0 0 0 0 0 0 0 1 0
# 0 8 0 9 0 0 0 0 0
# 0 0 7 0 4 0 6 0 3
# 0 0 3 0 6 0 5 0 4
# 0 0 0 0 0 0 0 0 2
# 7 0 0 0 0 3 0 0 0


# Ans :
# 1  7  5  3  8  9  4  2  6
# 9  3  2  4  7  6  1  8  5
# 4  6  8  5  1  2  3  7  9
# 3  5  4  6  2  7  9  1  8
# 6  8  1  9  3  5  2  4  7
# 2  9  7  1  4  8  6  5  3
# 8  2  3  7  6  1  5  9  4
# 5  1  6  8  9  4  7  3  2
# 7  4  9  2  5  3  8  6  1

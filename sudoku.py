import math
from numpy import matrix as m
from array import array


#-------------------------------------------------------------------|
#-------------- this part isn't a part of the solution--------------|
#-------------------------------------------------------------------|
    
def selectRow (mat, row):
    return mat [row]

def selectColumn (mat, column):
    return [row[column] for row in mat]

#-------------- to select a square from a Sudoku--------------
def selectSquare (mat, square):
    rows = selectRows (mat,square)
    li = []
    for i in range(len (rows)):
        li.append (selectColumns (rows[i], square))
    return li 

def selectColumns(row, i):
    size = root (len (row))
    row = row [ ((i % (size)) * size) : ]
    return row [: size]

def selectRows (mat,i):
    size = root (len (mat))
    mat = mat [ ((i // (size)) * size) : ]
    return mat [: size]

#-------------- to select a square from a Sudoku--------------

#-------------------------------------------------------------------|
#-------------- this part isn't a part of the solution--------------|
#-------------------------------------------------------------------|


#-------------------------------------------------------------------|
#--------------------------- START SOLUTION ------------------------|
#-------------------------------------------------------------------|

#-------------- checking for a valid Sudoku--------------
def root (num):
    return math.floor(math.sqrt(num))


def isValidSudoku(mat, num, pos):
    roo = root (len (mat))

    # Check row
    for i in range(len(mat[0])):
        if mat[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(mat)):
        if mat[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    sq_x = pos[1] // roo
    sq_y = pos[0] // roo

    for i in range(sq_y * roo, sq_y * roo + roo):
        for j in range(sq_x * roo, sq_x * roo + roo):
            if mat[i][j] == num and (i,j) != pos:
                return False

    return True


#-------------- checking for a valid Sudoku--------------

#-------------- solving Sudoku--------------

# modify the sudoku to set new value in (x,y) position
def setCell(mat, x, y, v):
    mat[x][y] = v 
    return mat 

def find_next_empty(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return (i, j)  # row, col

    return None


def solve_sudoku(mat):
    find = find_next_empty(mat)
    # if there no more empty celles then our sudoku is solved 
    if not find:
        return True
    else:
        x, y = find 
    
    for i in range (1, len(mat) + 1):
        
        if isValidSudoku (mat, i, (x, y)):
            setCell(mat, x, y, i)

            if solve_sudoku(mat):
                return True
            setCell(mat, x, y, 0)

    return False 
#-------------- solving Sudoku--------------

def print_board(mat):
    roo = root (len (mat))

    for i in range(len(mat)):
        #to print lines between each 3 lines
        if i % roo == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(mat[0])):
            #to print a vertical line each 3 columns 
            if j % roo == 0 and j != 0:
                print(" | ", end="")

            if j == len(mat)-1:
                print(mat[i][j])
            else:
                print(str(mat[i][j]) + " ", end="")

#-------------------------------------------------------------------|
#--------------------------- START SOLUTION ------------------------|
#-------------------------------------------------------------------|

mat4 = [[0,4,0,0,   8,0,16,0,   11,0,1,0,   0,6,0,14],
        [3,0,0,9,   0,15,0,4,    10,7,0,13,    0,0,12,0],
        [0,6,0,0,   2,11,0,0,    8,0,0,0,    3,0,0,0],
        [15,0,0,0,   0,0,0,13,    0,0,14,0,    0,2,0,4],

        [0,0,0,8,   0,3,0,0,    7,0,0,0,    5,0,0,0],
        [0,0,0,0,   0,0,14,0,    0,0,0,10,    0,16,0,13],
        [0,0,9,2,   5,0,0,0,    0,8,0,0,    11,0,0,0],
        [12,0,1,0,   0,0,0,16,    0,0,13,0,    0,0,3,0],

        [0,0,0,12,   15,0,0,0,    0,6,0,0,    13,0,4,7],
        [16,1,13,0,   10,0,0,3,    0,0,7,0,    0,9,0,0],
        [6,0,0,0,   0,0,11,0,    4,0,0,9,    0,0,2,10],
        [0,3,0,0,   0,16,0,0,    0,14,8,0,    0,11,0,0],

        [5,11,3,10,   0,0,0,8,    0,0,12,4,    0,0,0,1],
        [0,14,0,0,   11,9,0,0,    0,13,15,0,    4,0,5,0],
        [13,0,4,0,   6,0,0,0,    0,0,0,2,    0,12,0,9],
        [0,12,0,16,   0,13,0,0,    0,1,0,0,    6,0,15,0]]


mat3 = [[8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,0,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]]

mat2 = [[0,3,0,1],
        [0,0,0,2],
        [0,2,0,0],
        [0,0,0,0]]

#print(selectColumn(mat,0))
print_board (mat4)
print("_______________________________")
solve_sudoku (mat4)
print_board(mat4)


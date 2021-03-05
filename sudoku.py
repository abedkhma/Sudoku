import math
from numpy import matrix as m
from array import array

def root (num):
    return math.floor(math.sqrt(num))
    
def selectRow (matrix, row):
    return matrix [row]

def selectColumn (matrix, column):
    return [row[column] for row in matrix]

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

def selectRows (row,i):
    size = root (len (row))
    row = row [ ((i // (size)) * size) : ]
    return row [: size]

#-------------- to select a square from a Sudoku--------------

#-------------- checking for a valid Sudoku--------------

def isValidSubsection(section):
    sec = zeroFree(section)
    if len (sec) == len (set (sec)):
        return True
    return False

# to remove all the zeros from our section to check for duplicate 
def zeroFree (section):
    m = []
    for i in range (len (section)):
        if section[i] != 0:
            m.append(section[i])
    return m


def isValidSudoku(mat):
    # concat all the lists to one list to check for valid numbers
    matrixAsVector = result = sum(mat, [])

    for i in range (matrixAsVector):
        if matrixAsVector[i] < 0 and matrixAsVector[i] > len (matrixAsVector):
            return False

    for i in range (len (mat)):
        if((not isValidSubsection (selectColumn (mat[i, i])) or 
        not isValidSubsection (selectRow (mat[i], i)) or 
        not isValidSubsection (selectSquare (mat[i], i)))):
            return False
    return True

#-------------- checking for a valid Sudoku--------------

# modify the sudoku to set new value in (x,y) position
def setCell(mat, x, y, v):
    mat[x][y] = v 
    return mat 

#-------------- solving Sudoku--------------

#def solveSudoku(mat):
#    return suSol (mat, 0, 0)

# def suSol (mat, x, y):
#     if x >= len (mat):
#         if isValidSudoku (mat):
#             return mat 
#         else: return []

#     elif y >= len (mat):
#         suSol (mat,x+1,0)

#     elif selectRow(mat,x)[y] != 0:
#         suSol (mat, x, y+1)

#     else:
#        findFirstNotNull(recursiveResults(mat, x, y))

# def recursiveResults(mat, x, y):
#     m = []
#     for i in range(len (mat)):
#             if isValidSudoku (setCell (mat, x, y, i)):
#                 m.append(suSol (setCell (mat, x, y, i), x, y+1))
#     findFirstNotNull(m)

# def findFirstNotNull(mat):
#     for i in range (len (mat)):
#         if mat[i] != []:
#             return mat[i]
#     return []
    


x = [[ 0,  1,  2,  3,  4,5,2,5,2,4],
        [ 5,  6,  7,  8,  9,2,5,9,0],
        [10, 11, 12, 13, 14,4,6,2,8],
        [15, 16, 17, 18, 19,34,6,83,3],
        [ 0,  1,  2,  3,  4,5,2,5,2,4],
        [ 65,  56,  73,  8,  9,22,54,95,2],
        [0, 11, 2, 3, 1,4,6,34,3],
        [ 7,  51,  23,  3,  42,54,62,65,52,44],
        [ 56,  66,  57,  28,  29,62,54,39,10]]

mat = [[8,0,0,0,0,0,0,0,0],
              [0,0,3,6,0,0,0,0,0],
              [0,7,0,0,9,0,2,0,0],
              [0,5,0,0,0,7,0,0,0],
              [0,0,0,0,4,5,7,0,0],
              [0,0,0,1,0,0,0,3,0],
              [0,0,1,0,0,0,0,6,8],
              [0,0,8,5,0,0,0,1,0],
              [0,9,0,0,0,0,4,0,0]]
print (solveSudoku(mat))


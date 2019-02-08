import sys
from SudokuGraph import *

#print("Hello", str(sys.argv))

def get_sudoku():
    sudoku_string = list(sys.argv[1].split("=")[1])
    k = 0
    sudoku = [[0 for x in range(0,4)] for y in range(0,4)]
    for i in range(0,4):
        for j in range(0,4):
            sudoku[i][j] = sudoku_string[k]
            k += 1
    return(sudoku)

def test():
    sudoku = get_sudoku()
    sdk_graph = SudokuGraph()
    return sdk_graph.goalTest(sudoku)

print(test())



    

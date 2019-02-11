import sys
from SudokuGraph import *
from PuzzleGraph import *
from graph_search import *
#print("Hello", str(sys.argv))

hex_dict = {
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15
}    

def get_puzzle():
    puzzle_string = list(sys.argv[2].split("=")[1])
    k = 0
    puzzle = [[0 for x in range(0,4)] for y in range(0,4)]
    for i in range(0,4):
        for j in range(0,4):
            if puzzle_string[k] != '.':
                puzzle[i][j] = hex_dict[puzzle_string[k]]
            k += 1
    return (puzzle)
                

def get_sudoku():
    sudoku_string = list(sys.argv[2].split("=")[1])
    print(sudoku_string)
    k = 0
    sudoku = [[0 for x in range(0,4)] for y in range(0,4)]
    for i in range(0,4):
        for j in range(0,4):
            if sudoku_string[k] != '.':
                sudoku[i][j] = int(sudoku_string[k])
            k += 1
    return(sudoku)

def test():
    sudoku = get_sudoku()
    print(sudoku)
    sdk_graph = SudokuGraph(sudoku)
    return graph_search(sdk_graph)
    #return sdk_graph.actions(sudoku)

def puzzle_fifteen():
    puzzle = get_puzzle()
    print(puzzle)
    puzzle_problem = fifteenPuzzle(puzzle)
    return graph_search(puzzle_problem)
    

def main():
    game = sys.argv[1]
    if (game == "sudoku"):
        print(test())
    elif (game == "fifteen"):
        print(game)
        print(puzzle_fifteen())
    else:
        print("Use: main.py [game] [game=string]")

main()
    

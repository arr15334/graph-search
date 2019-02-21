import math

def copy_puzzle(p):
    the_copy = [[0 for x in range(0,4)] for y in range(0,4)]
    for i in range(0,4):
        for j in range(0,4):
            the_copy[i][j] = p[i][j]
    return the_copy

def manhattan_distance(x, i, j):
    correct_i = math.floor((x-0.01)/4)
    correct_j = (x % 4 - 1) if (x%4 != 0) else 3
    return (abs(i - correct_i) + abs(j - correct_j))
    
def possible_move(s, i, j):
    move = []
    if (j < 3):
        copy = copy_puzzle(s)
        copy[i][j], copy[i][j+1] = copy[i][j+1], copy[i][j]
        move.append(copy)
    if (j > 0):
        copy = copy_puzzle(s)
        copy[i][j], copy[i][j-1] = copy[i][j-1], copy[i][j]
        move.append(copy)
    if (i < 3):
        copy = copy_puzzle(s)
        copy[i][j], copy[i+1][j] = copy[i+1][j], copy[i][j]
        move.append(copy)
    if (i > 0):
        copy = copy_puzzle(s)
        copy[i][j], copy[i-1][j] = copy[i-1][j], copy[i][j]
        move.append(copy)
    return move

class fifteenPuzzle(object):
    def __init__(self, s):
        self.initial_state = s

    def actions(self, s):
        possible_moves = []
        for i in range(0,4):
            for j in range(0,4):
                if s[i][j] == 0:
                    for move in possible_move(s,i,j):
                        if move not in possible_moves:
                            possible_moves.append(move)
        return possible_moves

    def result(self, s, a):
        new_state = a
        return new_state

    def goal_test(self, s):
        index = 1
        for i in range(0,4):
            for j in range(0,4):
                if s[i][j] != index and index != 16:
                    return False
                index += 1
        return True

    def stepCost(self, a, possible_s):
        return 1

    def path_cost(self, path):
        return len(path)

    def h (self, puzzles):
        last_puzzle = puzzles[len(puzzles)-1]
        m_distance = 0
        misplaced_blocks = 0
        linear_conflicts = 0
        for i in range(0,4):
            for j in range(0,4):
                number = last_puzzle[i][j] #if last_puzzle[i][j] != 0 else 16
                number_c = last_puzzle[j][i]
                if (i*4 + (j+1) != number ): #and number > 0):
                    misplaced_blocks += 1
                m_distance += manhattan_distance(number, i, j) if number > 0 else 0
                if number <= (i+1)*4 and number > i * 4 and number != i*4 + (j+1) and number != 0 and j > 0:
                    correct_j = number % 4 - 1
                    if (correct_j < j):
                        for k in range(correct_j,j):
                            previous_number = last_puzzle[i][k]
                            if (previous_number <= (i+1)*4 and previous_number > i * 4 and previous_number != 0):
                                linear_conflicts += 1
                if (number_c % 4 == i + 1 and number_c != j*4 + (i+1) and number != 0 and j > 0):
                    correct_row = None
                    if (number_c <= 4):
                        correct_row = 0
                    elif(number_c <= 8):
                        correct_row = 1
                    elif(number_c <= 12):
                        correct_row = 2
                    else:
                        correct_row = 3
                    if (correct_row < j):                        
                        for k in range(correct_row, j):
                            previous_number = last_puzzle[j][k]
                            if (previous_number % 4 == i + i and previous_number != 0):
                                linear_conflicts += 1
        return max(m_distance + 2*linear_conflicts, misplaced_blocks)
        

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
        for i in range(0,4):
            for j in range(0,4):
                number = last_puzzle[i][j] #if last_puzzle[i][j] != 0 else 16
                if (i*4 + (j+1) != number and number > 0):
                    misplaced_blocks += 1
                m_distance += manhattan_distance(number, i, j) if number > 0 else m_distance
        return max(m_distance, misplaced_blocks)
        """
        missing = 0
        correct_next = 0
        distance = 0
        index = 1
        for i in range(0,4):
            for j in range(0,4):
                if (j != 3 and last_puzzle[i][j] + 1 == last_puzzle[i][j+1]):
                    correct_next += 1
                if (last_puzzle[i][j] != index):
                    missing += 1
                if (last_puzzle[i][j] == 0):
                    distance = 3 - i + 3 - j
                index += 1
        return 2*missing + distance - 2*correct_next
        """

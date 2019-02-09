def get_grid(i, j, s):
    if (i <= 1 and j <= 1):
        return [s[0][0], s[0][1], s[1][0], s[1][1]]
    elif (i <= 1 and j >1):
        return [s[0][2], s[0][3], s[1][2], s[1][3]]
    elif(i > 1 and j <= 1):
        return [s[2][0], s[2][1], s[3][0], s[3][1]]
    else:
        return [s[2][2], s[2][3], s[3][2], s[3][3]]

def possible_move(s, i, j):
        possible_entry = [1,2,3,4]
        curr_grid = get_grid(i, j, s)
        for n in range(1,5):
            if n in s[i]:
                print("remove", n, "by row")
                possible_entry.remove(n)
            else:
                the_column = [] 
                for c in s[0]:
                    if c != 0:
                        the_column.append(s[n-1][c-1])
                if n in the_column:
                    print("remove", n, "by column")
                    possible_entry.remove(n)
                else:
                    if (n in curr_grid):
                        print("remove", n, "by grid")
                        possible_entry.remove(n)
        print(possible_entry)
        return possible_entry


class SudokuGraph(object):
    all_sdk = [1,2,3,4]
    def __init__(self, s):
        self.initial_state = s

    def actions(self, s):
        print("action")
        act = []
        for i in range(0,4):
            for j in range(0,4):
                if s[i][j] == 0:
                    # devolver solo las posibles
                    entries = possible_move(s, i, j)
                    for n in entries:
                        print(n)
                        copy_sudoku = s.copy()
                        copy_sudoku[i][j] = n
                        possible_action = copy_sudoku
                        if possible_action not in (act):
                            act.append(possible_action)
        return act

    def result(self, s, a):
        new_state = 0
        return new_state

    def goal_test(self, s):
        sdku_num = [[0 for x in range(0,4)] for y in range(0,4)]
        for i in range(0,4):
            for j in range(0,4):
                if s[i][j] == 0:
                    return False
                else:
                    sdku_num[i][j] = int(s[i][j])
        print(sdku_num)
        # revisar todas las filas
        for i in range(0,4):
            if not(sum(sdku_num[i]) == 10 and all(x in sdku_num[i] for x in all_sdk)):
                print(sdku_num[i])
                print("suma")
                return False
        if (not checkColumns(self, s)):
            return False
        # revisar 4 mini grids  
        return True

    def stepCost(self, a, possible_s):
        return 1

    def path_cost(self, states):
        return len(states)

    def checkColumns(self, state):
        col_amount = len(state[0])
        for i in range(0, col_amount):
            curr_col = []
            for j in range(0, col_amount):
                curr_col.append(state[j][i])
            if not all(x in curr_col for x in all_sdk):
                return False
        return True

    def checkGrid(self, state):
        size = 1 if len(state[0] == 4) else 3
        start = 0
        for i in range(start, size):
            curr_grid = []
            for j in range(start, size):
                curr_grid.append(state[i][j])
            if not all(x in curr_grid for x in all_sdk):
                return False
            size += 1
            # 00 01 10 11 / 02 03 12 13 / 20 21 30 31 / 22 23 32 33
            # 00 01 02 10 11 12 20 21 22 / 03 04 05 13 14 15 23 24 25 / 
        return size



# [1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]
# [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]
#
    def h (self, s):
        empty = 0
        for i in len(s)-1:
            for j in len(s[i]-1):
                if (s[i][j] == '.'):
                    empty += 1
        return empty

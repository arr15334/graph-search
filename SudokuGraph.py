class SudokuGraph(object):
    all_sdk = [1,2,3,4]
    def __init__(self):
        self.initial_state = []

    def actions(self, s):
        act = []
        for i in range(0,4):
            for j in range(0,4):
                if s[i][j] == ".":
                    copy_sudoku = s.copy()
                    copy_sudoku[i][j] = j
                    possible_action = s
                    if possible_action not in (act):
                        act.append(possible_action)
        return act

    def result(self, s, a):
        new_state = 0
        return new_state

    def goalTest(self, s):
        sdku_num = [[0 for x in range(0,4)] for y in range(0,4)]
        for i in range(0,4):
            for j in range(0,4):
                if s[i][j] == ".":
                    print("punto")
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

    def pathCost(self, states):
        return 0

    def checkColumns(self, state):
        col_amount = len(state[0])
        for i in range(0, col_amount):
            curr_col = []
            for j in range(0, col_amount):
                curr_col.append(state[i][j])
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
            # 00 01 02 10 11 12 20 21 22 / 
        return size


# [1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]
# [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]
# 

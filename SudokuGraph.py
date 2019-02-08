class SudokuGraph(object):
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
        all_sdk = [1,2,3,4]
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
        # revisar todas las columnas
        #for i in range(0,4):
            #return
        # revisar 4 mini grids  
        return True

    def stepCost(self, a, possible_s):
        return 1

    def pathCost(self, states):
        return 0

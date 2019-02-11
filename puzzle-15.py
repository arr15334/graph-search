class fifteenPuzzle(object):
    def __init__(self, s):
        self.initial_state = s

    def actions(self, s):
        pass

    def result(self, s, a):
        new_state = a
        return new_state

    def goal_test(self, s):
        index = 1
        for i in range(0,4):
            for j in range(0,4):
                if s[i][j] != index:
                    return False
                index += 1
        return True

    def stepCost(self, a, possible_s):
        return 1

    def path_cost(self, path):
        return len(path)

    def h (self, puzzles):
        return 0

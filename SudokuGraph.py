class SudokuGraph(object):
    def __init__(self):
        self.initial_state = []

    def actions(self, s):
        a = []
        return a

    def result(self, s, a):
        new_state = 0
        return new_state

    def goalTest(self, s):
        return False

    def stepCost(self, a, possible_s):
        return 0

    def pathCost(self, states):
        return 0

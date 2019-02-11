def get_grid(i, j, s):
    if (i <= 1 and j <= 1):
        return [s[0][0], s[0][1], s[1][0], s[1][1]]
    elif (i <= 1 and j >1):
        return [s[0][2], s[0][3], s[1][2], s[1][3]]
    elif(i > 1 and j <= 1):
        return [s[2][0], s[2][1], s[3][0], s[3][1]]
    else:
        return [s[2][2], s[2][3], s[3][2], s[3][3]]

def get_grid_by_index(index, s):
    if (index == 0):
        return get_grid(0,0,s)
    elif (index == 1):
        return get_grid(0,2,s)
    elif (index == 2):
        return get_grid(2,0,s)
    elif (index == 3):
        return get_grid(3,3,s)

def possible_move(s, i, j):
        possible_entry = [1,2,3,4]
        curr_grid = get_grid(i, j, s)
        for n in range(1,5):
            if n in s[i]:
                #print("remove", n, "by row")
                possible_entry.remove(n)
            else:
                the_column = [] 
                for c in range(0,len(s[0])):
                    the_column.append(s[c][j])
                if n in the_column:
                    #print("remove", n, "by column")
                    possible_entry.remove(n)
                else:
                    if (n in curr_grid):
                        #print("remove", n, "by grid")
                        possible_entry.remove(n)
        #print(possible_entry)
        return possible_entry

def copy_sudoku(s):
    the_copy = [[0 for x in range(0,len(s[0]))] for y in range(0, len(s[0]))]
    for i in range(0, len(s[0])):
        for j in range(0, len(s[0])):
            the_copy[i][j] = s[i][j]
    return the_copy

class SudokuGraph(object):
    def __init__(self, s):
        self.initial_state = s
        self.all_sdk = [1,2,3,4] if len(s[0]) == 4 else [1,2,3,4,5,6,7,8,9]

    def actions(self, s):
        #print("action")
        act = []
        for i in range(0,len(s[0])):
            for j in range(0,len(s[0])):
                if s[i][j] == 0:
                    # devolver solo las posibles
                    entries = possible_move(s, i, j)
                    for n in entries:
                        a_copy = copy_sudoku(s)
                        a_copy[i][j] = n
                        if a_copy not in (act):
                            act.append(a_copy)
        return act

    def result(self, s, a):
        new_state = a
        return new_state
    
    def checkColumns(self, state):
        col_amount = len(state[0])
        for i in range(0, col_amount):
            curr_col = []
            for j in range(0, col_amount):
                curr_col.append(state[j][i])
            if not all(x in curr_col for x in self.all_sdk):
                return False
        return True

    def checkGrid(self, state):
        for i in range(0, len(state[0])):
            curr_grid = get_grid(i,i,state)
            if not all(x in curr_grid for x in self.all_sdk):
                return False
        return True

    def goal_test(self, s):
        for i in range(0,4):
            for j in range(0,4):
                if s[i][j] == 0:
                    return False

        # revisar todas las filas
        for i in range(0,len(s[0])):
            if not(all(x in s[i] for x in self.all_sdk)):
                print("suma")
                return False
        if (not self.checkColumns(s)):
            return False
        if (not self.checkGrid(s)):
            return False
        return True

    def stepCost(self, a, possible_s):
        return 1

    def path_cost(self, sudokus):
        #return 1
        return len(sudokus)

# [1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]
# [1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]
#
    def h (self, sudokus):
        last_sudoku = sudokus[len(sudokus)-1]
        empty_cells = 0
        full_rows = 0
        full_grids = 0
        full_columns = 0
        for i in range(0,len(last_sudoku[0])):
            current_column = []
            if (all(x in last_sudoku[i] for x in self.all_sdk)):
                full_rows += 1
            for j in range(0,len(last_sudoku[0])):
                if (last_sudoku[i][j] == 0):
                    empty_cells += 1
                current_column.append(last_sudoku[j][i])
            if (all (x in current_column for x in self.all_sdk)):
                full_columns +=1
            if (all (x in get_grid_by_index(i, last_sudoku) for x in self.all_sdk)):
                full_grids += 1
        return 2 * empty_cells - 3 * (full_rows + full_grids + full_columns)

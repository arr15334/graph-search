def get_grid(i, j, s):
    if (i <= 1 and j <= 1):
        return [s[0][0], s[0][1], s[1][0], s[1][1]]
    elif (i <= 1 and j >1):
        return [s[0][2], s[0][3], s[1][2], s[1][3]]
    elif(i > 1 and j <= 1):
        return [s[2][0], s[2][1], s[3][0], s[3][1]]
    else:
        return [s[2][2], s[2][3], s[3][2], s[3][3]]

def get_grid_9(i, j, s):
    if (i <= 2 and j <= 2):
        return [s[0][0], s[0][1], s[0][2],s[1][0], s[1][1], s[1][2], s[2][0], s[2][1], s[2][2]]
    elif (i <= 2 and j <= 5):
        return [s[0][3], s[0][4], s[0][5], s[1][3], s[1][4], s[1][5], s[2][3], s[2][4], s[2][5]]
    elif(i <= 2 and j > 5):
        return [s[0][6], s[0][7], s[0][8], s[1][6], s[1][7], s[1][8], s[2][6], s[2][7], s[2][8]]
    elif (i <= 5 and j <= 2):
        return [s[3][0], s[3][1], s[3][2],s[4][0], s[4][1], s[4][2], s[5][0], s[5][1], s[5][2]]
    elif (i <= 5 and j <= 5):
        return [s[3][3], s[3][4], s[3][5], s[4][3], s[4][4], s[4][5], s[5][3], s[5][4], s[5][5]]
    elif (i <= 5 and j > 5):
        return [s[3][6], s[3][7], s[3][8],s[4][6], s[4][7], s[4][8], s[5][6], s[5][7], s[5][8]]
    elif (i > 5 and j <= 2):
        return [s[6][0], s[6][1], s[6][2],s[7][0], s[7][1], s[7][2], s[8][0], s[8][1], s[8][2]]
    if (i > 5 and j <= 5):
        return [s[6][3], s[6][4], s[6][5],s[7][3], s[7][4], s[7][5], s[8][3], s[8][4], s[8][5]]
    else:
        return [s[6][6], s[6][7], s[6][8],s[7][6], s[7][7], s[7][8], s[8][6], s[8][7], s[8][8]]

def get_grid_by_index(index, s):
    if (index == 0):
        return get_grid(0,0,s)
    elif (index == 1):
        return get_grid(0,2,s)
    elif (index == 2):
        return get_grid(2,0,s)
    elif (index == 3):
        return get_grid(3,3,s)

def get_grid_by_index_9(index, s):
    if (index == 0):
        return get_grid_9(0,0,s)
    elif (index == 1):
        return get_grid_9(0,3,s)
    elif (index == 2):
        return get_grid_9(0,6,s)
    elif (index == 3):
        return get_grid_9(3,0,s)
    elif (index == 4):
        return get_grid_9(3,3,s)
    elif (index == 5):
        return get_grid_9(3,6,s)
    elif (index == 6):
        return get_grid_9(6,0,s)
    elif (index == 7):
        return get_grid_9(6,3,s)
    elif (index == 8):
        return get_grid_9(6,0,s)

def possible_move(s, i, j):
    size = len(s[0])
    possible_entry = [1,2,3,4] if size == 4 else [1,2,3,4,5,6,7,8,9]
    curr_grid = get_grid(i, j, s) if size == 4 else get_grid_9(i,j,s)
    possible_cell = []
    for n in range(1,size+1):
        if n in s[i]:
            #print("remove", n, "by row")
            possible_entry.remove(n)
        else:
            the_column = [] 
            for c in range(0,size):
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
        self.size = len(s[0])
        self.all_sdk = [1,2,3,4] if len(s[0]) == 4 else [1,2,3,4,5,6,7,8,9]

    def actions(self, s):
        #print("action")
        act = []
        cell_entry = []
        for i in range(0,self.size):
            for j in range(0,self.size):
                if s[i][j] == 0:
                    # devolver solo las posibles
                    entries = possible_move(s, i, j)
                    """
                    for n in entries:
                        a_copy = copy_sudoku(s)
                        a_copy[i][j] = n
                        if a_copy not in (act):
                            act.append(a_copy)
                    """
                    if (self.size == 9 and len(entries) == 1):
                        for n in entries:
                            a_copy = copy_sudoku(s)
                            a_copy[i][j] = n
                            if a_copy not in (act):
                                act.append(a_copy)
                    elif (self.size == 4):
                        for n in entries:
                            a_copy = copy_sudoku(s)
                            a_copy[i][j] = n
                            if a_copy not in (act):
                                act.append(a_copy)
        if (len(act) == 0 and self.size == 9):
            for i in range(0,self.size):
                for j in range(0,self.size):
                    if s[i][j] == 0:
                        # devolver solo las posibles
                        entries = possible_move(s, i, j)
                        for n in entries:
                            a_copy = copy_sudoku(s)
                            a_copy[i][j] = n
                            if a_copy not in (act):
                                act.append(a_copy)
        return act

    def actions2(self, s):
        actions = []
        cell_entry = [[[] for x in range(0,self.size)] for y in range(0,self.size)]
        for i in range(0,self.size):
            for j in range(0,self.size):
                if (s[i][j] == 0):
                    entries = possible_move(s,i,j)
                    for n in entries:
                        cell_entry[i][j].append(n)
        for i in range(0,self.size):
            for j in range(0,self.size):
                current_cell_options = cell_entry[i][j]
                row = cell_entry[i]
                grid = get_grid_9(i,j,cell_entry)
                column = [row[j] for row in cell_entry]
                options = current_cell_options.copy()
                for k in cell_entry[i][j]:
                    for r in row:
                        if (k in r) and k in options and r != options:
                            options.remove(k)
                    for c in column:
                        if (k in c) and k in options and c != options:
                            options.remove(k)
                    for g in grid:
                        if (k in g) and k in options and g != options:
                            options.remove(k)
                cell_entry[i][j] = options

        for i in range(0,self.size):
            for j in range(0,self.size):
                entries = cell_entry[i][j]
                for n in entries:
                    if (n != 0):
                        a_copy = copy_sudoku(s)
                        a_copy[i][j] = n
                        if a_copy not in actions:
                            actions.append(a_copy)
        print(actions)
        return actions

        
    def result(self, s, a):
        new_state = a
        return new_state
    
    def checkColumns(self, state):
        for i in range(0, self.size):
            curr_col = []
            for j in range(0, self.size):
                curr_col.append(state[j][i])
            if not all(x in curr_col for x in self.all_sdk):
                return False
        return True

    def checkGrid(self, state):
        for i in range(0, self.size):
            curr_grid = get_grid_by_index(i,state) if self.size == 4 else get_grid_by_index_9(i,state)
            if not all(x in curr_grid for x in self.all_sdk):
                return False
        return True

    def goal_test(self, s):
        for i in range(0,self.size):
            for j in range(0,self.size):
                if s[i][j] == 0:
                    #print("empty")
                    return False

        # revisar todas las filas
        for i in range(0,self.size):
            if not(all(x in s[i] for x in self.all_sdk)):
                #print("suma")
                return False
        if (not self.checkColumns(s)):
            #print("col")
            return False
        if (not self.checkGrid(s)):
            #print("grid")
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
        possibilities = 0
        for i in range(0,len(last_sudoku[0])):
            current_column = []
            if (all(x in last_sudoku[i] for x in self.all_sdk)):
                full_rows += 1
            for j in range(0,len(last_sudoku[0])):
                if (last_sudoku[i][j] == 0):
                    possibilities += len(possible_move(last_sudoku, i, j))
                    empty_cells += 1
                current_column.append(last_sudoku[j][i])
            if (all (x in current_column for x in self.all_sdk)):
                full_columns +=1
            if (self.size == 4):
                if (all (x in get_grid_by_index(i, last_sudoku) for x in self.all_sdk)):
                    full_grids += 1
            elif (self.size == 9):
                if (all (x in get_grid_by_index_9(i, last_sudoku) for x in self.all_sdk)):
                    full_grids += 1
        return empty_cells + possibilities #- 3 * (full_rows + full_grids + full_columns)
        #return 2 * empty_cells + possibilities - 3 * (full_rows + full_grids + full_columns)


        def h2 (self, sudokus):
            last_sudoku = sudokus[len(sudokus)-1]
            for i in range(0,self.size):
                for j in range(0,self.size):
                    p = possible_move(last_sudoku, i, j)
                    
                    row = last_sudoku[i]
                    current_grid = get_grid_9(i,j,last_sudoku)
                    column = [row[j] for row in last_sudoku]
                    



            

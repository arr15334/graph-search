from SudokuGraph import *

def a_star(frontier, problem):
    shortest = None
    for path in frontier:
        if not shortest or problem.path_cost(shortest) + problem.h(shortest) > problem.path_cost(path) + problem.h(path):
            shortest = path
    return shortest

def is_explored(path, res, e):
    pass

def copy_path(path):
    copy = []
    for p in path:
        copy.append(p)
    return copy

def graph_search(problem):
    frontier = [[problem.initial_state]]
    explored = []
    i = 0
    while True:
        i += 1
        #print(i)
        if i > 10000:
            print("not possible")
            print(path)
            return False
        elif i % 100 == 0:
            print(path)
        if (len(frontier)):
            path = a_star(frontier, problem)
            s = path[len(path)-1]
            frontier.remove(path)
            explored.append(s)
            if problem.goal_test(s):
                print("SOLVED")
                return path
            for a in problem.actions(s):
                #print(a)
                result = problem.result(s, a)
                #print(result)
                if result not in explored:
                    #print("explored", explored)
                    new_path = []
                    new_path = copy_path(path)
                    new_path.append(result)
                    frontier.append(new_path)
                #if not is_explored(path, result, explored):
                    #new_path = Path([])
                    #new_path.extendFrom(path)
                    #new_path.addStep(problem.result(s,a))
                 #   frontier.append(new_path)
        else:
            print("whot")
            print(path)
            return False



    


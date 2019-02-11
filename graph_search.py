from SudokuGraph import *

def a_star(frontier, problem):
    shortest = None
    for path in frontier:
        if not shortest or problem.path_cost(shortest) + problem.h(shortest) > problem.path_cost(path) + problem.h(path):
            shortest = path
    return shortest

def is_explored(path, res, e):
    pass

def graph_search(problem):
    frontier = [[problem.initial_state]]
    explored = []
    i = 0
    while i < 20:
        i += 1
        if (len(frontier)):
            path = a_star(frontier, problem)
            #print("frontier", frontier)
            #print("path", path)
            s = path[len(path)-1]
            explored.append(s)

            if problem.goal_test(s):
                print("SOLVED")
                return path

            for a in problem.actions(s):
                result = problem.result(s, a)
                print("result", result)
                if result not in explored:
                    print("explored", explored)
                    new_path = []
                    new_path = path.copy()
                    new_path.append(result)
                    frontier.append(new_path)
                #if not is_explored(path, result, explored):
                    #new_path = Path([])
                    #new_path.extendFrom(path)
                    #new_path.addStep(problem.result(s,a))
                 #   frontier.append(new_path)
        else:
            return False



    


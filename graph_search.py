from SudokuGraph import *

def graph_search(problem):
    frontier = [Path([problem.initial_state])]
    explored = []

    while True:
        if (len(frontier)):
            path = a_star(frontier, problem)
            s = path[len(path)-1]
            explored.append(path)

            if problem.goal_test(s):
                return path

            for a in problem.actions(s):
                result = problem.results(s, a)

                if not is_explored(path, result, explored):
                    new_path = Path([])
                    new_path.extendFrom(path)
                    new_path.addStep(problem.result(s,a))
                    frontier.append(new_path)
        else:
            return False

def a_star(frontier, problem):
    shortest = None
    for path in frontier:
        if not shortest or problem.path_cost(shortest) + problem.h(shortest) > problem.path_cost(path) + problem.h(path):
            shortest = path
    return shortest

    


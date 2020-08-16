import util

_FILL_IN_ = None


class BacktrackingSearch(util.SearchAlgorithm):
    def __init__(self, verbose=0):
        self.verbose = verbose
        
    def recurrence(self, state, path, path_cost):
        if self.verbose >= 2:
            print('state %s with path %s [%d]'%(state, path, path_cost))
        self.num_visited += 1
        
        # Check end condition
        if self.problem.is_end(state):
            if self.verbose >= 1:
                print('... new path %s [%d]'%(path, path_cost))
            if self.best_path is None or _FILL_IN_:  # HINT: compare path_cost with self.best_path_cost
                self.best_path, self.best_path_cost = tuple(path), path_cost
        
        # Find minimum cost path
        else:
            for action, next_state, action_cost in self.problem.succ_and_cost(state):
                path.append(action)  # extend path
                extended_path_cost = path_cost + action_cost
                _FILL_IN_  # HINT: call self.recurrence
                path.pop()      # recover path

    def solve(self, problem):
        # Not thread-safe
        self.problem = problem
        self.num_visited = 0
        self.best_path, self.best_path_cost = None, None
        
        initial_state = problem.start_state()
        empty_path = []
        self.recurrence(initial_state, empty_path, 0)
        
        return self.best_path, self.best_path_cost, self.num_visited

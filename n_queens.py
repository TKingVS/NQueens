# is_valid_state
# returns True if state is valid, meaning it
# has no queens in the same row, column, or diagonal
# otherwise returns false
def is_valid_state(state):
        for col in range(len(state)):
                if state[col] == -1:
                        break
                for prev_col in range(col):
                        # check row for two queens
                        if state[col] == state[prev_col]:
                                return False
                        # check downward diagonal for two queens
                        if state[col] == state[prev_col] + col - prev_col:
                                return False
                        if state[col] == state[prev_col] - col + prev_col:
                                return False
        return True

# goal_test
# returns True if state is a goal state, meaning
# it is valid and all queens are placed
def goal_test(state):
        if is_valid_state(state):
                for row in state:
                        if row == -1:
                                return False
                return True
        return False

# get_next
# determines what the next state should be after state
# start determines what row to start with in the next column
# returns the next state or None if no valid states are found
def get_next(state, start):
        for col in range(len(state)):
                if state[col] == -1:
                        for row in range(start, len(state)):
                                new_state = (*state[:col], row, *state[col + 1:])
                                if is_valid_state(new_state):
                                        return new_state
                        return None
                        
# solve_nqueens
# solves the nqueens problem for n queens
# returns the solution state
def solve_nqueens(n = 8):
        stack = [(-1,) * n]
        low_bound = 0
        col = 0

        while not goal_test(stack[-1]):

                # current state is last element in stack
                state = stack[-1]

                # no more valid positions for this column
                if low_bound >= n:
                        col = col - 1
                        low_bound = state[col] + 1
                        stack.pop()
                        continue

                # get next state
                next_state = get_next(state, low_bound)

                # next state is valid
                if (next_state):
                        col = col + 1
                        stack.append(next_state)
                        low_bound = 0
                # no valid next state
                else:
                        col = col - 1
                        low_bound = state[col] + 1
                        stack.pop()

        return stack[-1]
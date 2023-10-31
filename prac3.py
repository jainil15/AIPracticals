from collections import deque
import copy


def dfs(initial_state, goal_state):
    visited = []
    stack = []
    if initial_state == goal_state:
        print(initial_state)
        return ["None"]
    stack.insert(0, [initial_state, []])
    while len(stack) != 0:
        current_state, path = stack.pop(0)
        if current_state == goal_state:
            print(current_state, "done")
            return path
        if current_state not in visited:
            visited.append(current_state)
            for k in generate_states(current_state):

                stack.insert(0, [k[0], path + k[1]])


def generate_states(state):
    states = []
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                if j - 1 >= 0:
                    temp_state = copy.deepcopy(state)
                    temp_state[i][j], temp_state[i][j - 1] = temp_state[i][j - 1], temp_state[i][j]
                    states.append([temp_state, ['LEFT']])

                if j + 1 < 3:
                    temp_state = copy.deepcopy(state)
                    temp_state[i][j], temp_state[i][j + 1] = temp_state[i][j + 1], temp_state[i][j]
                    states.append([temp_state, ['RIGHT']])

                if i - 1 >= 0:
                    temp_state = copy.deepcopy(state)
                    temp_state[i][j], temp_state[i - 1][j] = temp_state[i - 1][j], temp_state[i][j]
                    states.append([temp_state, ['UP']])

                if i + 1 < 3:
                    temp_state = copy.deepcopy(state)
                    temp_state[i][j], temp_state[i + 1][j] = temp_state[i + 1][j], temp_state[i][j]
                    states.append([temp_state, ['DOWN']])
    return states


def main():
    goal_state = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]
    initial_state = [[1, 2, 3],
                     [4, 5, 6],
                     [7, 0, 8]]
    path = dfs(initial_state, goal_state)
    print(path)


if __name__ == "__main__":
    main()

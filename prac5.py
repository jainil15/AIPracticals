from collections import deque
import copy


def h(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            row = state[i][j] // 3
            col = state[i][j] % 3
            distance += col + row
    return distance


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


def astar(initial_state, goal_state):
    open_list = []
    closed_list = []

    open_list.append([initial_state, 0, h(initial_state, goal_state), []])

    while open_list:
        open_list.sort(key=lambda x: x[1] + x[2])
        current_state, g, h_value, path = open_list.pop(0)

        if current_state == goal_state:
            return path

        closed_list.append(current_state)

        for next_state, action in generate_states(current_state):
            if next_state in closed_list:
                continue
            g_next = g+1
            h_next = h(next_state, goal_state)
            f_next = g_next + h_next

            in_open = False
            open_list.append([next_state, g_next, h_next, path + action])




def main():
    goal_state = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]
    initial_state = [[1, 3, 6],
                     [4, 2, 0],
                     [7, 5, 8]]
    path = astar(initial_state, goal_state)
    print(path)


if __name__ == "__main__":
    main()

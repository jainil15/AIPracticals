from collections import deque
import copy


def h(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j]:
                distance+=1
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

    open_list.append([initial_state, 0, h(initial_state), []])

    while open_list:
        current_state = initial_state


def main():
    goal_state = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 0]]
    initial_state = [[1, 5, 7],
                     [4, 2, 6],
                     [3, 0 ,8]]
    path = h(initial_state, goal_state)
    print(path)
    print(h(initial_state, goal_state))





if __name__ == "__main__":
    main()

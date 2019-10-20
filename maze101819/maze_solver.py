from queue import Queue
from copy import deepcopy

MAZE_ARRAY = [
[6, 2, 1, 3, 6, 1, 7, 7, 4, 3],
[2, 3, 4, 5, 7, 8, 1, 5, 2, 3],
[1, 6, 1, 2, 5, 1, 6, 3, 6, 2],
[5, 3, 5, 5, 1, 6, 7, 3, 7, 3],
[1, 2, 6, 4, 1, 3, 3, 5, 5, 5],
[2, 4, 6, 6, 6, 2, 1, 3, 8, 8],
[2, 4, "*", 2, 3, 6, 5, 2, 4, 6],
[3, 1, 7, 6, 2, 3, 1, 5, 7, 7],
[6, 1, 3, 6, 4, 5, 4, 2, 2, 7],
[6, 7, 5, 7, 6, 2, 4, 1, 9, 1]
]

def search_maze(maze, start):
    maze_with_visitation_marks = []
    for row in maze:
        row_with_visitation_marks = []
        for value in row:
            row_with_visitation_marks.append([value, False])
        maze_with_visitation_marks.append(row_with_visitation_marks)
    
    search_queue = Queue()
    search_queue.put([start])
    while not search_queue.empty(): 
        path_to_explore = search_queue.get()
        node_to_explore = path_to_explore[-1]
        maze_with_visitation_marks[node_to_explore[0]][node_to_explore[1]][1] = True
        if maze_with_visitation_marks[node_to_explore[0]][node_to_explore[1]][0] == "*":
            return path_to_explore

        up_node = (node_to_explore[0] - maze_with_visitation_marks[node_to_explore[0]][node_to_explore[1]][0],
                node_to_explore[1])
        if up_node[0] >= 0 and not maze_with_visitation_marks[up_node[0]][up_node[1]][1]:
            up_node_path = deepcopy(path_to_explore)
            up_node_path.append(up_node)
            search_queue.put(up_node_path)

        left_node = (node_to_explore[0],
                node_to_explore[1] - maze_with_visitation_marks[node_to_explore[0]][node_to_explore[1]][0])
        if left_node[1] >= 0 and not maze_with_visitation_marks[left_node[0]][left_node[1]][1]:
            left_node_path = deepcopy(path_to_explore)
            left_node_path.append(left_node)
            search_queue.put(left_node_path)
        
        down_node = (node_to_explore[0] + maze_with_visitation_marks[node_to_explore[0]][node_to_explore[1]][0],
                node_to_explore[1])
        if down_node[0] < len(maze_with_visitation_marks) and not maze_with_visitation_marks[down_node[0]][down_node[1]][1]:
            down_node_path = deepcopy(path_to_explore)
            down_node_path.append(down_node)
            search_queue.put(down_node_path)

        right_node = (node_to_explore[0],
                node_to_explore[1] + maze_with_visitation_marks[node_to_explore[0]][node_to_explore[1]][0])
        if right_node[1] < len(maze_with_visitation_marks[right_node[0]]) and not maze_with_visitation_marks[right_node[0]][right_node[1]][1]:
            right_node_path = deepcopy(path_to_explore)
            right_node_path.append(right_node)
            search_queue.put(right_node_path)

    return []

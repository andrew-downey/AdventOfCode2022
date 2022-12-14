#!/usr/bin/env python3
import os
from time import time
from colorama import Style
from collections import defaultdict

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    start: tuple[int, int]
    end: tuple[int, int]
    start_height = ord('a')
    end_height = ord('z')
    grid: dict[int, dict[int, int]] = dict()
    for y in range(len(rows)):
        grid[y] = {}
        for x in range(len(rows[y])):
            if rows[y][x] == 'S':
                start = (y, x)
                value = start_height
            elif rows[y][x] == 'E':
                end = (y, x)
                value = end_height
            else:
                value = ord(rows[y][x])

            grid[y][x] = value

    print("Initial map")
    for y, i in grid.items():
        for x, j in i.items():
            tup = (y, x)
            print(f"{Style.BRIGHT if (tup == end or tup == start) else Style.DIM} {j:>3}{Style.RESET_ALL}", end='')
        print()
    print(Style.RESET_ALL)


    y, x = start
    graph = defaultdict(dict)
    # Add an edge for each neighbour
    for y, row in grid.items():
        for x, new_height in row.items():
            for ny, nx in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                if(y + ny < len(grid) and y + ny >= 0 and x + nx < len(grid[0]) and x + nx >= 0):
                    graph[(y, x)][(y + ny, x + nx)] = new_height

    visited = {start: start_height}
    parents = {}
    queue = {start: start_height}
    while len(queue) > 0:
        # cache stack is empty or invalid, nullify it and find the minimum
        current_cost = min(queue.values())
        current_cost_index = list(queue.values()).index(current_cost)
        current_node = list(queue.keys())[current_cost_index]

        for neighbour, cost in graph[current_node].items():
            height_difference = grid[neighbour[0]][neighbour[1]] - grid[current_node[0]][current_node[1]]
            if neighbour not in visited and height_difference <= 1:
                new_cost = 99999
                try:
                    new_cost = queue[neighbour]
                except KeyError:
                    pass
                candidate_cost = current_cost + cost
                if candidate_cost < new_cost:
                    queue[neighbour] = candidate_cost
                    parents[neighbour] = current_node

        visited[current_node] = current_cost
        del queue[current_node]

        # for y, i in grid.items():
        #     for x, j in i.items():
        #         tup = (y, x)
        #         print(f"{Style.BRIGHT if (tup in visited) else Style.DIM} {j:>3}{Style.RESET_ALL}", end='')
        #     print()
        # print()

        if(current_node == end):
            break

    node = end
    backpath = [end]
    path = []
    while node != start:
        backpath.append(parents[node])
        node = parents[node]
    for i in range(len(backpath)):
        path.append(backpath[-i - 1])

    print(len(path) - 1)
    print(path)

    # # [print(f"{len(path)} {path}") for path in global_paths]
    # for path in range(min(len(global_paths), 3)):
    #     print(f"{path} ({len(global_paths[path] - 1)} steps)")
    #     for y, i in grid.items():
    #         for x, j in i.items():
    #             tup = (y, x)
    #             print(f"{Style.BRIGHT if (tup in global_paths[path]) else Style.DIM} {j:>3}{Style.RESET_ALL}", end='')
    #         print()
    #     print()



if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

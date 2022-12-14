#!/usr/bin/env python3
import os
from time import time
from colorama import Style

start: tuple[int, int]
target_point: tuple[int, int]
global_paths: list[tuple[int, int]] = []

def explore(grid: dict[int, dict[int, int]], current_pos: tuple[int, int]):
    visited.append(current_pos)

    #     for y, i in grid.items():
    #         for x, j in i.items():
    #             tup = (y, x)
    #             print(f"{Style.BRIGHT if (tup in visited) else Style.DIM} {'#' if (tup in visited) else '.'}{Style.RESET_ALL}", end='')
    #         print()
    #     print()

    y, x = current_pos
    current_height = grid[y][x]
    for ny, nx in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
        if (ny, nx) not in visited and nx >= 0 and ny >= 0 and nx < len(grid[0]) and ny < len(grid):
            new_height = grid[ny][nx]
            if abs(current_height - new_height) <= 1:
                queue.append((ny, nx))

    global target_point
    visited = {}
    queue = {(0, 0): 0}
    while len(queue) > 0:
            # cache stack is empty or invalid, nullify it and find the minimum
            current_cost = min(queue.values())
            minimums_cache_stack = []
            current_cost_index = list(queue.values()).index(current_cost)
            current_node = list(queue.keys())[current_cost_index]

        for neighbour, cost in graph[current_node].items():
            if neighbour not in visited:
                new_cost = MAXINT
                try:
                    new_cost = queue[neighbour]
                except KeyError:
                    pass
                candidate_cost = current_cost + cost
                if candidate_cost < new_cost:
                    queue[neighbour] = candidate_cost
                    if new_cost <= current_minimum:
                        current_minimum = new_cost

        visited[current_node] = current_cost
        del queue[current_node]

        if(current_node == target_point):
            break

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    global start
    global end
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

    explore(grid, start, [])

    global global_paths
    global_paths = sorted(global_paths, key=lambda path: len(path))

    # [print(f"{len(path)} {path}") for path in global_paths]
    for path in range(min(len(global_paths), 3)):
        print(f"{path} ({len(global_paths[path] - 1)} steps)")
        for y, i in grid.items():
            for x, j in i.items():
                tup = (y, x)
                print(f"{Style.BRIGHT if (tup in global_paths[path]) else Style.DIM} {j:>3}{Style.RESET_ALL}", end='')
            print()
        print()




if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

#!/usr/bin/env python3
import math
import os
from time import time
from colorama import Style

start: tuple[int, int]
end: tuple[int, int]
def explore(steps: int, grid: dict[int, dict[int, int]], current_pos: tuple[int, int]):
    global start
    global end
    if current_pos == end or current_pos == start:
        return steps

    if steps > 200:
        return None

    steps += 1
    next_neighbours = [(y, x) for y, i in grid.items() for x, j in i.items() if math.abs(y - current_pos[0] <= 1 or math.abs(x - current_pos[1] <= 1))]

    paths = []
    for pos in next_neighbours:
        paths.append(explore(steps, grid, pos))

    return paths

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../example.txt')
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

    for y, i in grid.items():
        for x, j in i.items():
            tup = (y, x)
            print(f"{Style.BRIGHT if (tup == end or tup == start) else Style.DIM} {j:>3}{Style.RESET_ALL}", end='')
        print()

    explore(0, grid, start)

    print(Style.RESET_ALL)




if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

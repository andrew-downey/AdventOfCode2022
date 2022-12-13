#!/usr/bin/env python3
import copy
import os
from time import time

class Point:
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    tail = Point(0,0)
    head = Point(0,0)
    positions: set[tuple[int, int]] = set()
    positions.add((tail.x, tail.y))

    # print("Initial state")
    # for y in range(-10, 10):
    #     for x in range(-10, 10):
    #         print(f"H" if head.x == x and head.y == y else "T" if tail.x == x and tail.y == y else "#" if (x,y) in positions else '.', end="")
    #     print()
    # print()

    for row in rows:
        print(row)
        direction, distance = row.split()
        for _ in range(int(distance)):
            if direction == 'R':
                head.x += 1
            elif direction == 'U':
                head.y += 1
            elif direction == 'L':
                head.x -= 1
            else:
                head.y -= 1

            new_tail = copy.deepcopy(tail)
            if head.x > tail.x + 1 or (head.x > tail.x and (head.y > tail.y + 1 or head.y < tail.y - 1)) :
                new_tail.x += 1
            if head.x < tail.x - 1 or (head.x < tail.x and (head.y > tail.y + 1 or head.y < tail.y - 1)):
                new_tail.x -= 1
            if head.y > tail.y + 1 or (head.y > tail.y and (head.x > tail.x + 1 or head.x < tail.x - 1)):
                new_tail.y += 1
            if head.y < tail.y - 1 or (head.y < tail.y and (head.x > tail.x + 1 or head.x < tail.x - 1)):
                new_tail.y -= 1

            tail = new_tail

            positions.add((tail.x, tail.y))

            # for y in range(10, -10, -1):
            #     for x in range(-10, 10):
            #         print(f"H" if head.x == x and head.y == y else "T" if tail.x == x and tail.y == y else "#" if (x,y) in positions else '.', end="")
            #     print()
            # print()

    print(f"Tail positions: {len(positions)}")




if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

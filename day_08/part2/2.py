#!/usr/bin/env python3
import os
from time import time
from collections import defaultdict
from colorama import Style

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    max_score = 0
    best_tree = (0,0)
    scores: list[list[int]] = []
    for y in range(len(rows)):
        scores.append([])
        for x in range(len(rows[y])):
            this_height = rows[y][x]
            left = list(reversed([height for height in rows[y][:x]]))
            right = [height for height in rows[y][x + 1:]]
            up = list(reversed([y[x] for y in rows[:y]]))
            down = [y[x] for y in rows[y + 1:] if y[x]]

            this_score = 1
            for direction in [left, right, up, down]:
                distance = 0
                for distance in range(len(direction)):
                    if int(direction[distance]) >= int(this_height):
                        break
                this_score *= distance + 1 if len(direction) > 0 else 0

            scores[y].append(this_score)
            if this_score > max_score:
                max_score = this_score
                best_tree = (y, x)

    for y in range(len(scores)):
        for x in range(len(scores[y])):
            if (y, x) == best_tree:
                print(f"{Style.BRIGHT} {str(scores[y][x]) : >6}", end = "")
            else:
                print(f"{Style.NORMAL} {str(scores[y][x]) : >6}", end ="")
        print()



    print()
    print(f"Max scenic score is {max_score}")



if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print()
    print(f'Finished in {round((end - start) * 1000, 5)} milliseconds')

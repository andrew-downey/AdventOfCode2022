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

    trees = 0
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            this_height = rows[y][x]
            left = len([height for height in rows[y][:x] if height >= this_height]) == 0
            right = len([height for height in rows[y][x + 1:] if height >= this_height]) == 0
            up = len([y[x] for y in rows[:y] if y[x] >= this_height]) == 0
            down = len([y[x] for y in rows[y + 1:] if y[x] >= this_height]) == 0
            if left or right or up or down:
                trees +=1
                print(Style.BRIGHT + this_height, end =" ")
            else:
                print(Style.NORMAL + this_height, end =" ")

        print(Style.RESET_ALL)

    print()
    print(f"There are {trees} visible trees")



if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print()
    print(f'Finished in {round((end - start) * 1000, 5)} milliseconds')

#!/usr/bin/env python3
import os
from time import time
from collections import defaultdict


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    current_elf = 1
    elves = defaultdict(int)
    for row in rows:
        if (row == ''):
            current_elf += 1
            continue
        elves[current_elf] += int(row)

    elves = {key: val for key, val in sorted(
        elves.items(), key=lambda ele: ele[1], reverse=True)}

    print("Elves: {0}".format(elves))


if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

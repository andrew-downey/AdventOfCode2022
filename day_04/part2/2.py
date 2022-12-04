#!/usr/bin/env python3
import os
from time import time


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    overlaps = 0
    for row in rows:
        elf: list[set] = []
        for assignment in row.split(','):
            lower, upper = assignment.split('-')
            elf.append(set([i for i in range(int(lower), int(upper) + 1)]))

        if(len(elf[0].intersection(elf[1])) > 0 or len(elf[1].intersection(elf[0])) > 0):
            overlaps+=1

    print(f"Overlaps: {overlaps}")


if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print(f'Finished in {round((end - start) * 1000, 5)} milliseconds')

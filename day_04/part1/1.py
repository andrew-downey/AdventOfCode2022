#!/usr/bin/env python3
import os
from time import time


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    reconsiderations = 0
    for row in rows:
        elf: list[set] = []
        for assignment in row.split(','):
            lower, upper = assignment.split('-')
            elf.append(set([i for i in range(int(lower), int(upper) + 1)]))

        if(elf[0].issubset(elf[1]) or elf[1].issubset(elf[0])):
            reconsiderations+=1

    print(f"Reconsiderations: {reconsiderations}")


if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

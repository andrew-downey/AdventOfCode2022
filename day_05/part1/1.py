#!/usr/bin/env python3
import os
from time import time
import re
from collections import defaultdict
from collections import deque


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    stacks = defaultdict(deque)
    for row in rows:
        if row.startswith('move'):
            command = [int(x) for x in re.findall(r"(\d+)", row)]
            for _ in range(1, command[0] + 1):
                if (len(stacks[command[1]]) > 0):
                    crate = stacks[command[1]].pop()
                    stacks[command[2]].append(crate)
        elif len(row) > 0 and not row.startswith(' 1'):
            crates = re.findall(r"(\w|\s\s\s\s)", row)
            for crate_id in range(len(crates)):
                if len(crates[crate_id]) == 1:
                    stacks[crate_id + 1].appendleft(crates[crate_id])

    stacks = {key: val for key, val in sorted(
        stacks.items(), key=lambda ele: ele[0])}
    print(stacks)

    string = ''
    for i in range(1, len(stacks) + 1):
        if (len(stacks[i]) > 0):
            string += stacks[i].pop()
    print(string)


if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

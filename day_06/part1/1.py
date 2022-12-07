#!/usr/bin/env python3
import os
from time import time
from collections import deque


def find_marker(input: str):
    for i in range(3, len(input) - 4):
        buff = input[i-4:i]
        count = sum([buff.count(char) for char in buff])
        if count == 4:
            return i

    return 0


def main():
    assert find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    assert find_marker('nppdvjthqldpwncqszvftbrmjlhg') == 6
    assert find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    assert find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    for row in rows:
        marker = find_marker(row)
        print(marker)


if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print(f'Finished in {round((end - start) * 1000, 5)} milliseconds')

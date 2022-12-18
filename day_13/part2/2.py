#!/usr/bin/env python3
import os
from time import time
from itertools import zip_longest
from functools import cmp_to_key

def compare(left, right, indent: int = 0):
    print(f"{'  ' * indent}- Compare {left} vs {right}")
    if left is None:
        print(f"{'  ' * indent}- left is None, returning True")
        return 1
    if right is None:
        print(f"{'  ' * indent}- right is None, returning False")
        return -1

    if isinstance(left, int) and isinstance(right, int):
        if left != right:
            print(f"{'  ' * indent}- Integers aren't equal, so {left < right}")
            return 1 if left < right else -1
        else:
            print(f"{'  ' * indent}- Integers are equal, so continue")
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        for new_left, new_right in zip_longest(left, right):
            result = compare(new_left, new_right, indent + 1)
            if result != 0:
                return result
        return 0
    else:
        print(f"{'  ' * indent}- Mixed types; convert to array and retry comparison")
        new_left = [left] if isinstance(left, int) else left
        new_right = [right] if isinstance(right, int) else right
        return compare(new_left, new_right, indent + 1)


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    packets = [eval(row) for row in rows if len(row) > 0]
    dividers = ([[2]], [[6]])
    packets.append(dividers[0])
    packets.append(dividers[1])

    packets.sort(key = cmp_to_key(compare), reverse=True)

    print()
    [print(packet) for packet in packets]

    div_one = packets.index(dividers[0]) + 1
    div_two = packets.index(dividers[1]) + 1
    print()
    print(f"Dividers located at {div_one} and {div_two}")
    print(f"Answer {div_one * div_two}")


if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

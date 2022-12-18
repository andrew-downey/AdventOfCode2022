#!/usr/bin/env python3
import os
from time import time
from itertools import zip_longest

def compare(left, right, indent: int = 0):
    print(f"{'  ' * indent}- Compare {left} vs {right}")
    if left is None:
        print(f"{'  ' * indent}- left is None, returning True")
        return True
    if right is None:
        print(f"{'  ' * indent}- right is None, returning False")
        return False

    if isinstance(left, int) and isinstance(right, int):
        if left != right:
            print(f"{'  ' * indent}- Integers aren't equal, so {left < right}")
            return left < right
        else:
            print(f"{'  ' * indent}- Integers are equal, so continue")
            return None
    elif isinstance(left, list) and isinstance(right, list):
        for new_left, new_right in zip_longest(left, right):
            result = compare(new_left, new_right, indent + 1)
            if result != None:
                return result
        return None
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

    packet_count = 0
    first_part = None
    second_part = None
    correct_packet_sum: int = 0
    packets = [row for row in rows if len(row) > 0]
    for i in range(0, len(packets), 2):
        packet_count += 1
        first_part = eval(packets[i])
        second_part = eval(packets[i + 1])
        print()
        result = compare(first_part, second_part)

        if result:
            correct_packet_sum += packet_count
        elif result == None:
            raise Exception(f"!!!!! No result determined for {first_part} Vs. {second_part}")

    print()
    print(f"Answer: {correct_packet_sum}")


if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

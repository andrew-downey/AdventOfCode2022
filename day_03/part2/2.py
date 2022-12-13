#!/usr/bin/env python3
import os
from time import time

def get_value(char: str):
    return ord(char) - (38 if char.isupper() else 96)

def main():
    assert get_value("a") == 1
    assert get_value("A") == 27
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    print(f"Rows: {rows}")

    carry = 0
    total = 0
    for row in rows:
        carry+=1
        current_comp = set(row)
        if carry == 1:
            comp_scratch = current_comp.copy()
        else:
            comp_scratch = comp_scratch.intersection(current_comp)

        print(f"Common chars: {[char for char in comp_scratch]}")

        if carry == 3:
            carry = 0
            total += get_value(list(comp_scratch)[0])
            print(f"Badge: {list(comp_scratch)[0]}")

    print(f"Total: {total}")


if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

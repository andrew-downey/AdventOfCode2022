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

    total = 0
    for row in rows:
        comp_one = set(row[0:len(row)//2])
        comp_two = set(row[len(row)//2:len(row)])
        diff = [char for char in comp_one if char in comp_two][0]
        diff_val = get_value(diff)
        total += diff_val
        print(f"Diff for row {row}: {diff} ({diff_val})")

    print(f"Total: {total}")


if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print(f'Finished in {round((end - start) * 1000, 5)} milliseconds')

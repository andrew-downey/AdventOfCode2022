#!/usr/bin/env python3
import os
from time import time


def find_marker(input: str):
    print(input)


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../example.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    for row in rows:
        find_marker(row)

    print(f"Rows: {rows}")


if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print(f'Finished in {round((end - start) * 1000, 5)} milliseconds')

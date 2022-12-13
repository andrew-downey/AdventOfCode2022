#!/usr/bin/env python3
import os
from time import time


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../example.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    print(f"Rows: {rows}")


if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

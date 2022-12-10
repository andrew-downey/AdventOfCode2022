#!/usr/bin/env python3
import os
from time import time
import re


class File:
    files: dict
    parent: str
    size: int

    def __init__(self) -> None:
        self.files = dict()

    def set_parent(self, parent):
        self.parent = parent
        return self

    def set_size(self, size):
        self.size = size
        return self


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    pointer = root = File()
    for row in rows:
        tokens = row.split(' ')
        if tokens[0] == '$':
            if tokens[1] == 'cd':
                target_dir = tokens[2]
                if target_dir == '/':
                    pointer = root
                elif target_dir == '..':
                    pointer = pointer.parent
                else:
                    pointer = pointer.files[target_dir]

        elif tokens[0] == 'dir':
            pointer.files[tokens[1]] = File().set_parent(pointer)
        else:
            pointer.files[tokens[1]] = File()\
                .set_parent(pointer)\
                .set_size(tokens[0])

    print(root)


if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print(f'Finished in {round((end - start) * 1000, 5)} milliseconds')

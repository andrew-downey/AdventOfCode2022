#!/usr/bin/env python3
import os
from time import time
import re

total = 0
class File:
    files: dict[str, 'File']
    parent: 'File' = None
    size: int = 0

    def __init__(self) -> None:
        self.files = dict()

    def set_parent(self, parent):
        self.parent = parent
        return self

    def set_size(self, size):
        self.size = int(size)
        return self

    def add_size(self, size):
        self.size += int(size)
        return self

    def recurse(self, filename:str, indent: int):
        if len(self.files) > 0:
            for name, file in self.files.items():
                file.recurse(name, indent+1)

        if self.parent:
            self.parent.add_size(self.size)

        print(f"{'!' if self.size <= 100000 and len(self.files) > 0 else ' '}{'  ' * indent} - {'(dir)' if len(self.files) > 0 else ''} {filename} ({'{:,}'.format(self.size)})")
        if self.size <= 100000 and len(self.files) > 0:
            global total
            total += self.size

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

    root.recurse('/', 1)
    print(f'\n Total: {total}')


if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print(f'Finished in {round((end - start) * 1000, 5)} milliseconds')

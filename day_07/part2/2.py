#!/usr/bin/env python3
import os
from time import time
import re

candidates: dict[str, 'File'] = dict()
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

    def recurse(self, filename: str, indent: int = 1):
        if len(self.files) > 0:
            for name, file in self.files.items():
                file.recurse(name, indent+1)

        if self.parent:
            self.parent.add_size(self.size)

        print(f"{'!' if self.size <= 100000 and len(self.files) > 0 else ' '}{'  ' * indent} - {'(dir)' if len(self.files) > 0 else ''} {filename} ({'{:,}'.format(self.size)})")

    def find_deletion_candidates(self, filename: str, candidate_size: int):
        if len(self.files) > 0 and self.size >= candidate_size:
            print(f'Adding deletion candidate "{filename}" ({"{:,}".format(self.size)})')
            global candidates
            candidates[filename] = self

        if len(self.files) > 0:
            for name, file in self.files.items():
                file.find_deletion_candidates(name, candidate_size)


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

    root.recurse('/')

    max_space = 70000000
    space_needed = 30000000
    used = max_space - root.size
    difference = space_needed - used
    print()
    print(f'Required space to be freed: {"{:,}".format(difference)}')

    root.find_deletion_candidates('/', difference)
    print(["{0} ({1})".format(name, '{:,}'.format(file.size)) for name, file in candidates.items()])


if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

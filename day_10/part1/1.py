#!/usr/bin/env python3
import os
from time import time
from collections import deque

OPS = {
    'addx': 2,
    'noop': 1
}

class CRT:
    def print(self):
        pass

class CPU:
    x: int
    # op, counter, value
    stack: deque[tuple[str, int, int]]

    def __init__(self) -> None:
        self.stack = deque()
        self.x = 1

    def tick(self) -> 'CPU':
        if(len(self.stack) == 0):
            return False

        if self.stack[0][1] == 0:
            command = self.stack.popleft()
            if command[0] == 'addx':
                self.x += command[2]

        if(len(self.stack) == 0):
            return False

        left_tuple = self.stack[0][0]
        right_tuple = self.stack[0][2]
        self.stack[0] = (left_tuple, self.stack[0][1] - 1, right_tuple)

        return True

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    cpu = CPU()
    for row in rows:
        bits = row.split()
        cpu.stack.append((bits[0], OPS[bits[0]], int(bits[1]) if len(bits) > 1 else None))
    del rows

    tick = 0
    total = 0
    while(cpu.tick()):
        tick += 1
        if (tick - 20) % 40 == 0 and tick <= 220:
            print(f"Tick {tick}:\n  - signal value: {cpu.x * tick} ({cpu.x})")
            total += cpu.x * tick

    print()
    print(f"Total at cycles 20-220: {total}")


if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

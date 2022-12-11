#!/usr/bin/env python3
import math
import os
from time import time
from collections import deque
import re

from colorama import Style

class Monkey:
    monkeys: list['Monkey']
    items: deque[int]
    operation: tuple[str, str, str]
    test: int
    truth_monkey: int
    false_monkey: int
    inspections: int = 0

    def __init__(self, monkeys: list['Monkey']) -> None:
        self.monkeys = monkeys
        self.items = deque()

    def turn(self, mod):
        for item_id in range(len(self.items)):
            self.items[item_id] = self.inspect(self.items[item_id])

        # print(f"  - Getting bored...")
        # for item in self.items:
        #     print(f"    - {item}")
        self.items = deque([item % mod for item in self.items])
        # for item in self.items:
        #     print(f"    - {item}")

        while self.items:
            self.throw(self.items.popleft())

    def inspect(self, item: int) -> int:
        self.inspections += 1
        old = item
        # print(f"  - Inspecting item {item}... ", end='')
        op_value = old if self.operation[2] == 'old' else int(self.operation[2])
        item = old * op_value if self.operation[1] == '*' else old + op_value
        # print(f"new value {item}")

        return item

    def throw(self, item: int) -> None:
        target = self.truth_monkey if item % self.test == 0 else self.false_monkey
        # print(f"  - Throwing item {item} to {target}")
        self.monkeys[target].items.append(item)



def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    monkeys: list[Monkey] = []
    for row in rows:
        if row == '':
            continue
        tokens = row.split()
        if tokens[0] == 'Monkey':
            monkeys.append(Monkey(monkeys))
            current_monkey = monkeys[len(monkeys) - 1]
        elif tokens[0] == 'Starting':
            items = re.findall('(\d+)', row)
            items = [int(item) for item in items]
            current_monkey.items.extend(items)
        elif tokens[0] == 'Operation:':
            current_monkey.operation = (tokens[3], tokens[4], tokens[5])
        elif tokens[0] == 'Test:':
            current_monkey.test = int(re.findall('(\d+)', row)[0])
        elif tokens[0] == 'If':
            if tokens[1] == 'true:':
                current_monkey.truth_monkey = int(tokens[5])
            else:
                current_monkey.false_monkey = int(tokens[5])

    mod = math.lcm(*[monkey.test for monkey in monkeys])
    print(f"Modulus is {mod}")
    rounds = 10000
    for round in range(0, rounds):
        for monkey in range(len(monkeys)):
            monkeys[monkey].turn(mod)

        if round % 1000 == 0 or round == 20 or round == 1:
            print()
            print(f"== After round {round} ==")
            [print(f'Monkey {monkey} inspected items {monkeys[monkey].inspections} times') for monkey in range(len(monkeys))]

    print()
    print("Results:")
    monkeys.sort(key = lambda monkey: -monkey.inspections)
    for monkey in monkeys:
        print(monkey.inspections)

    print()
    print(f"Answer: {Style.BRIGHT}{monkeys[0].inspections * monkeys[1].inspections}")
    print(Style.RESET_ALL)


if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print(f'Finished in {round((end - start) * 1000, 5)} milliseconds')

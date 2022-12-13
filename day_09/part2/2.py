#!/usr/bin/env python3
import copy
import os
from time import time

positions: set[tuple[int, int]] = set()

class Point:
    x: int
    y: int

    def set_pos(self, x, y) -> 'Point':
        self.x = x
        self.y = y

        return self

class Rope:
    knots: list[Point]

    def __init__(self) -> None:
        self.knots = []

    def move_head(self, x, y) -> 'Rope':
        head = self.knots[0]
        head.set_pos(head.x + x, head.y + y)

        for knot in self.knots[1:]:
            new_knot = copy.deepcopy(knot)
            if head.x > knot.x + 1 or (head.x > knot.x and (head.y > knot.y + 1 or head.y < knot.y - 1)) :
                new_knot.x += 1
            if head.x < knot.x - 1 or (head.x < knot.x and (head.y > knot.y + 1 or head.y < knot.y - 1)):
                new_knot.x -= 1
            if head.y > knot.y + 1 or (head.y > knot.y and (head.x > knot.x + 1 or head.x < knot.x - 1)):
                new_knot.y += 1
            if head.y < knot.y - 1 or (head.y < knot.y and (head.x > knot.x + 1 or head.x < knot.x - 1)):
                new_knot.y -= 1

            knot.set_pos(new_knot.x, new_knot.y)
            head = knot

        global positions
        positions.add((self.knots[9].x, self.knots[9].y))
        return self

    def print(self):
        for y in range(10, -10, -1):
            for x in range(-20, 20):
                symbol = "#" if (x,y) in positions else '.'
                for knot_id in range(1, len(self.knots)):
                    if self.knots[knot_id].x == x and self.knots[knot_id].y == y:
                        symbol = knot_id
                        break

                if self.knots[0].x == x and self.knots[0].y == y:
                    symbol = 'H'

                print(symbol, end="")
            print()
        print()

def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    rope = Rope()
    num_knots = 10
    for _ in range(num_knots):
        rope.knots.append(Point().set_pos(0,0))

    print("Initial state")
    rope.print()

    for row in rows:
        print(row)
        direction, distance = row.split()

        x = 0
        y = 0
        if direction == 'R':
            x += 1
        elif direction == 'U':
            y += 1
        elif direction == 'L':
            x -= 1
        else:
            y -= 1

        for _ in range(int(distance)):
            rope.move_head(x, y)#.print()

    print(f"Tail positions: {len(positions)}")




if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

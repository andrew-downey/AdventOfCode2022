#!/usr/bin/env python3
import os
from time import time

playmap = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

winmap = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

drawmap = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

losemap = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../input.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    score = 0
    for row in rows:
        row = row.split(' ')
        my_play = ''
        if row[1] == 'X':
            my_play = losemap.get(row[0])
        elif row[1] == 'Y':
            my_play = drawmap.get(row[0])
        else:
            my_play = winmap.get(row[0])

        score += playmap[my_play]

        if winmap.get(row[0]) == my_play:
            score += 6
        elif drawmap.get(row[0]) == my_play:
            score += 3

    print("Score: {0}".format(score))


if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

#!/usr/bin/env python3
import os
from time import time

ints = []
def compare(left, right, indent: int = 0):
    result = None

    print(f"{' ' * indent}Comparing:\n  {left}\n  {right}")
    for i, part_l in enumerate(left):
        if i >= len(right):
            result = False
            break
        part_r = right[i]

        if isinstance(part_l, int) and isinstance(part_r, int):
            if part_l == part_r:
                result = None
            else:
                result = part_l < part_r

            break
        elif isinstance(part_l, list) and isinstance(part_r, list):
            nested_result = compare(part_l, part_r, indent + 1)
            if nested_result != None:
                result = nested_result
                break
        else:
            if isinstance(part_l, list):
                nested_result = compare(part_l, [part_r], indent + 1)
            else:
                nested_result = compare([part_l], part_r, indent + 1)

            if nested_result != None:
                result = nested_result
                break

    if result == None:
        result = len(left) > len(right)

    print(f"{' ' * indent}{result}")
    return result

def nested_sum(packets: list):
    numbers = []
    for bit in packets:
        if isinstance(bit, int):
            numbers.append(bit)
        else:
            numbers.append(nested_sum(bit))

    return sum(numbers)


def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../example.txt')
    with open(filename, "r") as myfile:
        rows = myfile.read().splitlines()

    packet_count = 0
    first_part = None
    second_part = None
    correct_packets:list[tuple[list[int], list[int]]] = []
    for i, row in enumerate(rows):
        if i % 3 == 0:
            first_part = eval(row)
        elif i % 3 == 1:
            second_part = eval(row)
            packet_count += 1
        else:
            result = compare(first_part, second_part)
            if result:
                correct_packets.append(packet_count)
            first_part = None
            second_part = None


    print("Correct packets: ")
    print(correct_packets)
    print(sum(correct_packets))
    # print(f"Answer: {nested_sum(correct_packets)}")



if __name__ == "__main__":
    challenge_start_time= time()
    main()
    challenge_end_time = time()
    print(f'Finished in {round((challenge_end_time  - challenge_start_time) * 1000, 5)} milliseconds')

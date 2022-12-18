import re
from collections import deque
from pathlib import Path

import numpy as np


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    droplets = {tuple(map(int, re.findall(r"(\d+)", coords))) for coords in input_data}

    free_sides = 0
    for drop in droplets:
        # check neighbors
        free_sides += 6
        for neighbor in [[+1, 0, 0], [-1, 0, 0], [0, +1, 0], [0, -1, 0], [0, 0, +1], [0, 0, -1]]:
            if tuple(np.array(drop) - np.array(neighbor)) in droplets:
                free_sides -= 1
    return free_sides


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    droplets = [tuple(map(int, re.findall(r"(\d+)", coords))) for coords in input_data]

    # Idea: Find the outside of the sphere
    Q = deque([(0, 0, 0)])
    rel_drops = set()
    seen = set()
    while len(Q) > 0:
        drop = Q.popleft()
        print(len(Q), len(rel_drops))
        seen.add(drop)

        for neighbor in [[+1, 0, 0], [-1, 0, 0], [0, +1, 0], [0, -1, 0], [0, 0, +1], [0, 0, -1]]:
            new_pixel = (drop[0] + neighbor[0], drop[1] + neighbor[1], drop[2] + neighbor[2])
            if new_pixel in droplets:
                rel_drops.add(drop)
            # if outside of field -> skip
            if any([c < 0 or c > 25 for c in new_pixel]) or new_pixel in seen or new_pixel in droplets:
                continue
            Q.append(new_pixel)

    print("Done flooding")
    print(rel_drops)
    free_sides = 0
    for drop in rel_drops:
        # check neighbors
        free_sides += 6
        for neighbor in [[+1, 0, 0], [-1, 0, 0], [0, +1, 0], [0, -1, 0], [0, 0, +1], [0, 0, -1]]:
            if tuple(np.array(drop) - np.array(neighbor)) in rel_drops:
                free_sides -= 1
    return free_sides


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 64

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 58

    result = part_2("input.txt")
    print(result)

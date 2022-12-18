import re
from pathlib import Path

import numpy as np


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    droplets = [list(map(int, re.findall(r"(\d+)", coords))) for coords in input_data]

    free_sides = 0
    for drop in droplets:
        # check neighbors
        free_sides += 6
        for neighbor in [[+1, 0, 0], [-1, 0, 0], [0, +1, 0], [0, -1, 0], [0, 0, +1], [0, 0, -1]]:
            if list(np.array(drop) - np.array(neighbor)) in droplets:
                free_sides -= 1
    return free_sides


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    droplets = [list(map(int, re.findall(r"(\d+)", coords))) for coords in input_data]

    droplets_array = np.array(droplets)
    area = 0
    # Idea: flooding algorithm
    for z in range(np.max(droplets_array, axis=2), np.min(droplets_array, axis=2), 1):
        pass

    return area


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

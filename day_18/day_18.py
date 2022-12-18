import re
from collections import deque
from pathlib import Path


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    droplets = {tuple(map(int, re.findall(r"(\d+)", coords))) for coords in input_data}

    free_sides = 0
    for drop in droplets:
        # check neighbors
        free_sides += 6
        for neighbor in get_neighbors(*drop):
            if neighbor in droplets:
                free_sides -= 1
    return free_sides


def get_neighbors(x: int, y: int, z: int) -> set:
    return {(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)}


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    droplets = [tuple(map(int, re.findall(r"(\d+)", coords))) for coords in input_data]

    # Idea: Find the outside of the sphere
    Q = deque([(-1, -1, -1)])
    seen = set()
    touching_surface = 0
    while len(Q) > 0:
        drop = Q.popleft()
        seen.add(drop)

        for neighbor in get_neighbors(*drop):
            # if outside of field -> skip
            if any([c < -1 or c > 25 for c in neighbor]) or neighbor in seen or neighbor in Q:
                continue
            # If the neighbor is a droplet -> increase count
            if neighbor in droplets:
                touching_surface += 1
                continue
            Q.append(neighbor)

    return touching_surface


if __name__ == "__main__":

    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 64
    result_ex = part_1("input_ex_2.txt")
    print(result_ex)
    assert result_ex == 108

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 58

    result_ex = part_2("input_ex_2.txt")
    print(result_ex)
    assert result_ex == 90

    result = part_2("input.txt")
    assert result > 2557
    print(result)

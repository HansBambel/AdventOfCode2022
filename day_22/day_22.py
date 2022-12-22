import re
from itertools import zip_longest
from pathlib import Path
from typing import Dict, List, Tuple

# Right, down, left, up
directions = [(0, +1), (+1, 0), (0, -1), (-1, 0)]


def build_cave(cave_map) -> Tuple[Dict[Tuple[int, int], str], Tuple[int, int]]:
    cave: Dict[Tuple[int, int], str] = {}
    start_pos = (0, 0)
    for row, line in enumerate(cave_map.split("\n")):
        for column, char in enumerate(line):
            if char in [".", "#"]:
                if row == 0 and char == ".":
                    start_pos = (row, column)
                cave[(row, column)] = char
    return cave, start_pos


def decode(encoded_code: str) -> List[Tuple[int, str]]:
    numbers = list(map(int, re.findall(r"(\d+)[LR]*", encoded_code)))
    letters = re.findall(r"\d*([LR])", encoded_code)

    return list(zip_longest(numbers, letters, fillvalue=""))


def wrap_around(cave, pos, facing) -> Tuple[int, int]:
    match facing:
        case 0:
            cur_pos = (pos[0], 0)
        case 1:
            cur_pos = (0, pos[1])
        case 2:
            max_x = max([x for y, x in cave.keys() if y == pos[0]])
            cur_pos = (pos[0], max_x)
        case 3:
            max_y = max([y for y, x in cave.keys() if x == pos[1]])
            cur_pos = (max_y, pos[1])
        case _:
            raise ValueError("Invalid value for facing: ", facing)
    while cave.get(cur_pos, None) is None:
        cur_pos = (cur_pos[0] + directions[facing][0], cur_pos[1] + directions[facing][1])

    return cur_pos


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    cave_map, encoded_code = data_file.split("\n\n")

    cave, cur_pos = build_cave(cave_map)
    code = decode(encoded_code)

    facing = 0
    for steps, turn in code:
        for _ in range(steps):
            # move(cave, cur_pos, facing)
            new_pos = (cur_pos[0] + directions[facing][0], cur_pos[1] + directions[facing][1])
            # check if new_pos is in cave. If not: wrap around
            if cave.get(new_pos, None) is None:
                new_pos = wrap_around(cave, cur_pos, facing)
            # in cave
            if cave[new_pos] == "#":
                break
            else:
                cur_pos = new_pos

        if turn == "R":
            facing += 1
            facing = facing % len(directions)
        elif turn == "L":
            facing -= 1
            facing = (len(directions) - 1) if facing < 0 else facing

    # calc score
    score = 1000 * (cur_pos[0] + 1) + 4 * (cur_pos[1] + 1) + facing
    return score


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 6032

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 5031

    result = part_2("input.txt")
    print(result)

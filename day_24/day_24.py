from functools import lru_cache
from pathlib import Path
from queue import Queue
from typing import Tuple

directions = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}


@lru_cache(maxsize=None)
def move_blizzards(
    blizzards: Tuple[Tuple[Tuple[int, int], Tuple[int, int]], ...], max_y: int, max_x: int
) -> Tuple[Tuple[Tuple[int, int], Tuple[int, int]], ...]:
    new_positions = []
    for pos, direction in blizzards:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if new_pos[0] < 1:
            new_pos = (max_y, new_pos[1])
        elif new_pos[0] > max_y:
            new_pos = (1, new_pos[1])
        if new_pos[1] < 1:
            new_pos = (new_pos[0], max_x)
        elif new_pos[1] > max_x:
            new_pos = (new_pos[0], 1)
        new_positions.append((new_pos, direction))
    return tuple(new_positions)


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    # (pos), (movement)
    blizzards = []
    for row, line in enumerate(input_data):
        for col, char in enumerate(line):
            if char in directions.keys():
                blizzards.append(((row, col), (directions[char])))
    blizzards = tuple(blizzards)
    cur_pos = (0, input_data[0].find("."))
    goal_pos = (len(input_data), input_data[-1].find("."))

    i = 0
    seen = {(cur_pos, blizzards)}
    prev = {}
    Q = Queue()
    # pos, blizzards, distance
    Q.put((cur_pos, blizzards, 0))
    while not Q.empty():
        cur_pos, blizzards, cur_dist = Q.get()
        if cur_pos == goal_pos:
            break
        blizzards = move_blizzards(blizzards, max_y=len(input_data) - 1, max_x=len(input_data[0]) - 1)
        blizz_pos = [pos for pos, _ in blizzards]
        # check possible moves from here
        for neighbor in directions.values():
            new_pos = (cur_pos[0] + neighbor[0], cur_pos[1] + neighbor[1])
            # if new_pos is occupied by a blizzard or is outside the grid don't add
            if new_pos in blizz_pos or (new_pos, blizzards) in seen:
                continue
            if new_pos == goal_pos or (0 < new_pos[0] < len(input_data) and 0 < new_pos[1] < len(input_data[0])):
                seen.add((new_pos, blizzards))
                prev[new_pos] = cur_pos
                Q.put((new_pos, blizzards, cur_dist + 1))

        i += 1

    print(cur_dist)
    # backtrack and count number of steps
    path = []
    cur_pos = goal_pos
    while prev.get(cur_pos, None):
        path.append(cur_pos)
        cur_pos = prev[cur_pos]
    return len(path)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 18

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 1337

    result = part_2("input.txt")
    print(result)

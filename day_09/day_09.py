from pathlib import Path
from typing import Set, Tuple


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    head_pos = [0, 0]
    tail_pos = [0, 0]
    tail_visited: Set[Tuple[int, int]] = {(0, 0)}
    for line in input_data:
        direction, num = line.split(" ")
        num = int(num)

        if direction == "U":
            axis, value = 0, 1
        elif direction == "D":
            axis, value = 0, -1
        elif direction == "L":
            axis, value = 1, -1
        else:
            axis, value = 1, 1
        for _ in range(num):
            head_pos[axis] += value
            if abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1:
                tail_pos[0] = tail_pos[0] + max(min(1, head_pos[0] - tail_pos[0]), -1)
                tail_pos[1] = tail_pos[1] + max(min(1, head_pos[1] - tail_pos[1]), -1)

            tail_visited.add(tuple(tail_pos))

    return len(set(tail_visited))


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    tail_visited: Set[Tuple[int, int]] = {(0, 0)}
    tails = [[0, 0] for _ in range(10)]
    for line in input_data:
        direction, num = line.split(" ")
        num = int(num)

        if direction == "U":
            axis, value = 0, 1
        elif direction == "D":
            axis, value = 0, -1
        elif direction == "L":
            axis, value = 1, -1
        else:
            axis, value = 1, 1
        # print(f"Instr: {line}")
        for _ in range(num):
            tails[0][axis] += value
            for i, tail in enumerate(tails):
                if i == 0:
                    continue
                prev_tail = tails[i - 1]
                if abs(prev_tail[0] - tail[0]) > 1 or abs(prev_tail[1] - tail[1]) > 1:
                    tail[0] = tail[0] + max(min(1, prev_tail[0] - tail[0]), -1)
                    tail[1] = tail[1] + max(min(1, prev_tail[1] - tail[1]), -1)

            # print(tails)
            tail_visited.add(tuple(tails[-1]))

    return len(set(tail_visited))


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 13

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    assert result == 1, result

    print("\n" + "#" * 10 + " Other example " + "#" * 10)
    result = part_2("input_ex2.txt")
    assert result == 36, result

    print("\n" + "#" * 10 + " Real input " + "#" * 10)
    result = part_2("input.txt")
    print(result)

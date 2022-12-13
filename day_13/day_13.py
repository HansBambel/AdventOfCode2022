from collections import deque
from pathlib import Path
from typing import Optional


def compare_left_right(left, right) -> Optional[bool]:

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif right < left:
            return False
        # Continue checking
        return None

    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            if i >= len(left) or i >= len(right):
                break
            cmp = compare_left_right(left[i], right[i])
            if cmp is None:
                continue
            return cmp

        # could be that list has len 0
        if len(left) == len(right):
            return None
        if len(left) < len(right):
            return True
        else:
            return False

    else:
        # Mixed types
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]
        return compare_left_right(left, right)


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    pairs = data_file.split("\n\n")
    sum_index = 0
    for i, pair in enumerate(pairs):
        left, right = pair.split("\n")
        correct_order = compare_left_right(eval(left), eval(right))
        if correct_order:
            sum_index += i + 1

    return sum_index


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    lines = data_file.replace("\n\n", "\n").split("\n")
    lines += ["[[2]]", "[[6]]"]

    lines_evaluated = [eval(line) for line in lines]
    # Write a sorting algorithm and reuse the compare function from earlier
    sorted_list = deque([lines_evaluated.pop()])
    for line in lines_evaluated:
        for i, sorted_line in enumerate(sorted_list):
            # True Left smaller
            # False right smaller
            # None both the same
            cmp = compare_left_right(sorted_line, line)
            if cmp is True:
                continue
            else:
                sorted_list.insert(i, line)
                break

    # find the 2 and 6 again
    indices = [i + 1 for i in range(len(sorted_list)) if sorted_list[i] in [[[2]], [[6]]]]
    return indices[0] * indices[1]


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 13

    result = part_1("input.txt")
    assert result > 1116, result
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 140

    result = part_2("input.txt")
    print(result)

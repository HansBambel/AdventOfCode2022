from pathlib import Path
from typing import Dict, Tuple


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    tree_map: Dict[Tuple[int, int], int] = {}
    for y, line in enumerate(input_data):
        for x in range(len(line)):
            tree_map[y, x] = int(line[x])

    visible = 0
    # Now check if trees are visible
    for (y, x), height in tree_map.items():
        # check until edge if trees before and after are <= as the current one
        tree_vis_left, tree_vis_right, tree_vis_top, tree_vis_bot = True, True, True, True
        diff = 1
        # If tree is on edge it is visible and does not need to be checked
        edge_tree = is_edge_tree(x, y, input_data)
        while not edge_tree and diff < max(len(input_data), len(input_data[0])):
            if height <= tree_map[(max(y - diff, 0), x)]:
                tree_vis_bot = False
            if height <= tree_map[min(y + diff, len(input_data) - 1), x]:
                tree_vis_top = False
            if height <= tree_map[(y, max(x - diff, 0))]:
                tree_vis_left = False
            if height <= tree_map[y, min(len(input_data) - 1, x + diff)]:
                tree_vis_right = False
            diff += 1

            if not tree_vis_right and not tree_vis_left and not tree_vis_top and not tree_vis_bot:
                break

        visible += tree_vis_left or tree_vis_right or tree_vis_top or tree_vis_bot

    return visible


def is_edge_tree(x: int, y: int, input_data) -> bool:
    return x == 0 or y == 0 or x == len(input_data[0]) - 1 or y == len(input_data) - 1


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    tree_map: Dict[Tuple[int, int], int] = {}
    for y, line in enumerate(input_data):
        for x in range(len(line)):
            tree_map[y, x] = int(line[x])

    highest = 0
    # Now check if trees are visible
    for (y, x), height in tree_map.items():
        # check until edge if trees before and after are <= as the current one
        trees_vis_left, trees_vis_right, trees_vis_top, trees_vis_bot = 0, 0, 0, 0
        tree_limit_left, tree_limit_right, tree_limit_top, tree_limit_bot = False, False, False, False
        diff = 1
        while not tree_limit_left and x - diff >= 0:
            trees_vis_left += 1
            if height <= tree_map[y, x - diff]:
                tree_limit_left = True
            diff += 1
        diff = 1
        while not tree_limit_right and x + diff <= len(input_data[0]) - 1:
            trees_vis_right += 1
            if height <= tree_map[y, x + diff]:
                tree_limit_right = True
            diff += 1
        diff = 1
        while not tree_limit_top and y - diff >= 0:
            trees_vis_top += 1
            if height <= tree_map[y - diff, x]:
                tree_limit_top = True
            diff += 1
        diff = 1
        while not tree_limit_bot and y + diff <= len(input_data) - 1:
            trees_vis_bot += 1
            if height <= tree_map[y + diff, x]:
                tree_limit_bot = True
            diff += 1
        diff = 1

        # while diff < max(len(input_data), len(input_data[0])):
        #     if not tree_limit_top and height <= tree_map[(max(y - diff, 0), x)]:
        #         tree_limit_top = True
        #         if not max(y - diff, 0) == y:
        #             trees_vis_top += 1
        #     if not tree_limit_bot and height <= tree_map[min(y + diff, len(input_data) - 1), x]:
        #         tree_limit_bot = True
        #         if not min(y + diff, len(input_data) - 1) == y:
        #             trees_vis_bot += 1
        #     if not tree_limit_left and height <= tree_map[(y, max(x - diff, 0))]:
        #         tree_limit_left = True
        #         if not max(x - diff, 0) == x:
        #             trees_vis_left += 1
        #     if not tree_limit_right and height <= tree_map[y, min(len(input_data) - 1, x + diff)]:
        #         tree_limit_right = True
        #         if not min(len(input_data) - 1, x + diff):
        #             trees_vis_right += 1
        #
        #     diff += 1

        score = trees_vis_left * trees_vis_right * trees_vis_top * trees_vis_bot
        if highest < score:
            highest = score

    return highest


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 21

    result = part_1("input.txt")
    assert result != 751
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 8

    result = part_2("input.txt")
    print(result)

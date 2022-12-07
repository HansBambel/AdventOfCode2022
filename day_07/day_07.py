import re
from pathlib import Path
from typing import Any, Dict


class Node:
    parent = None
    files: Dict[str, int]
    dirs: Dict[str, Any]

    def __init__(self, parent=None):
        self.parent = parent
        self.files = {}
        self.dirs = {}

    def calc_size(self):
        total = 0
        for size in self.files.values():
            total += size
        for dir_node in self.dirs.values():
            dir_size = dir_node.calc_size()
            total += dir_size
        return total


def calc_dir_size(node: Node) -> int:
    total = 0
    # for size in node.files.values():
    #     total += size
    for dir_node in node.dirs.values():
        dir_size = dir_node.calc_size()
        if dir_size <= 100_000:
            total += dir_size

        total += calc_dir_size(dir_node)
    return total


def build_tree(data) -> Node:
    root = Node()
    current = root
    for line in data:
        if line.startswith("$"):
            if "cd .." in line:
                # go one up
                current = current.parent
            elif "cd /" in line:
                # go to root
                current = root
            elif "cd" in line:
                # enter directory
                dir_name = re.findall(r"\$ cd (.*)", line)[0]
                current = current.dirs[dir_name]
            else:
                # ls
                pass

        elif line.startswith("dir"):
            dir_name = re.findall(r"dir (.*)", line)[0]
            new_node = Node(parent=current)
            current.dirs[dir_name] = new_node
        else:
            # filesize + name
            size, name = re.findall(r"(\d+) (.*)", line)[0]
            current.files[name] = int(size)
    return root


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    root = build_tree(input_data)

    # Get dir sizes
    total = calc_dir_size(root)
    return total


def find_enough_space(current: Node, to_delete: int):
    """Recursively find the biggest directory to delete."""
    if current.calc_size() < to_delete:
        return None
    min_dir = current.calc_size()
    for dirs in current.dirs.values():
        dir_size = find_enough_space(dirs, to_delete)
        if dir_size is not None and to_delete <= dir_size < min_dir:
            min_dir = dir_size
    return min_dir


def part_2(input_file: str):
    max_size = 70_000_000
    goal_free = 30_000_000
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    root = build_tree(input_data)
    min_del = root.calc_size()
    # find node that if deleted frees up enough space
    to_delete = abs(max_size - goal_free - min_del)
    min_dir = find_enough_space(root, to_delete)
    return min_dir


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 95437

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 24933642

    result = part_2("input.txt")
    assert result != 4259939
    print(result)

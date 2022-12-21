import itertools
from pathlib import Path

from tqdm import tqdm


class Element:
    value: int
    before = None
    after = None

    def __init__(self, value, before=None, after=None):
        self.value = value
        self.before = before
        self.after = after

    def __str__(self):
        return f"{self.value}"


class LinkedList:
    current: Element
    last: Element
    start: Element
    length = 0

    def __init__(self):
        self.current = None
        self.last = None
        self.start = None

    def append(self, value):
        new_elem = Element(value, before=self.current, after=self.current)
        if self.current is None:
            new_elem.after = new_elem
            new_elem.before = new_elem
            self.start = new_elem
        else:
            new_elem.before = self.current
            new_elem.after = self.current.after
            self.current.after = new_elem
        self.last = new_elem
        self.current = new_elem
        self.length += 1


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = list(map(int, data_file.split("\n")))

    linked_list = [Element(val) for val in input_data]
    for before, after in itertools.pairwise(linked_list):
        before.after = after
        after.before = before

    linked_list[0].before = linked_list[-1]
    linked_list[-1].after = linked_list[0]

    for elem in tqdm(linked_list):

        # rest = abs(elem.value) % (len(arr)-1)
        if elem.value < 0:
            nums = range(elem.value, 0, 1)
        else:
            nums = range(elem.value)
        elem.before.after = elem.after
        elem.after.before = elem.before
        current = elem.before
        for _ in nums:
            if elem.value < 0:
                current = current.before
            else:
                current = current.after

        # insert the element again
        elem.before = current
        elem.after = current.after
        current.after = elem
        elem.after.before = elem

    # find the 0
    elem = linked_list[0]
    while elem.value != 0:
        elem = elem.after

    # add 1000th, 2000th, 3000th after 0 together
    total = 0
    for i in range(1, 3001):
        elem = elem.after
        if i % 1000 == 0:
            total += elem.value

    return total


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 3

    result = part_1("input.txt")
    assert result < 6153, result
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 1623178306

    result = part_2("input.txt")
    print(result)

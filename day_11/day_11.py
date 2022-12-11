from pathlib import Path
from typing import List, Tuple

from tqdm import tqdm


class Monkey:
    items: List[int]
    operation_str: Tuple[str, str]
    divisor: int
    inspected_items: int
    true_monkey: int
    false_monkey: int

    def __init__(self):
        self.items = []
        self.inspected_items = 0

    def operation(self, old: int) -> int:
        self.inspected_items += 1
        if self.operation_str[1].isnumeric():
            other = int(self.operation_str[1])
        else:
            other = old
        if self.operation_str[0] == "*":
            return old * other
        elif self.operation_str[0] == "+":
            return old + other
        elif self.operation_str[0] == "-":
            return old - other

    def throw(self, num: int, monkeys: List["Monkey"]):
        if num % self.divisor == 0:
            monkeys[self.true_monkey].items.append(num)
        else:
            monkeys[self.false_monkey].items.append(num)


def parse_monkeys(data_file):
    monkey_input = data_file.split("\n\n")
    # parse monkeys
    monkeys = []
    for monkey in monkey_input:
        monkey_lines = monkey.split("\n")
        new_monkey = Monkey()
        for line in monkey_lines:
            if "Starting items: " in line:
                new_monkey.items = [int(num) for num in line.split("Starting items: ")[1].split(", ")]
            if "Operation: " in line:
                op = line.split("new = old ")[1]
                new_monkey.operation_str = op.split(" ")
            if "Test: " in line:
                new_monkey.divisor = int(line.split("divisible by ")[1])
            if "If true: throw to monkey " in line:
                new_monkey.true_monkey = int(line.split("If true: throw to monkey ")[1])
            if "If false: throw to monkey " in line:
                new_monkey.false_monkey = int(line.split("If false: throw to monkey ")[1])
        monkeys.append(new_monkey)
    return monkeys


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    monkeys = parse_monkeys(data_file)

    for _ in range(20):
        # go through monkeys
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                item = monkey.items.pop(0)
                item = monkey.operation(item)
                item = item // 3
                monkey.throw(item, monkeys)

    monkey_business = sorted([monkey.inspected_items for monkey in monkeys], reverse=True)
    return monkey_business[0] * monkey_business[1]


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    monkeys = parse_monkeys(data_file)

    for _ in tqdm(range(10000)):
        # go through monkeys
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                item = monkey.items.pop(0)
                item = monkey.operation(item)
                # item = item // 3
                monkey.throw(item, monkeys)

    monkey_business = sorted([monkey.inspected_items for monkey in monkeys], reverse=True)
    return monkey_business[0] * monkey_business[1]


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 10605

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 2713310158

    result = part_2("input.txt")
    print(result)

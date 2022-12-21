from pathlib import Path
from typing import Any, Dict

monkeys: Dict[str, Any] = {}


def get_number(monkey: str) -> int:
    if isinstance(monkeys[monkey], float):
        return monkeys[monkey]
    m1, op, m2 = monkeys[monkey]
    num1, num2 = get_number(m1), get_number(m2)
    match op:
        case "+":
            res = num1 + num2
        case "-":
            res = num1 - num2
        case "*":
            res = num1 * num2
        case "/":
            res = num1 / num2
    return res


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    global monkeys
    for line in input_data:
        name, rest = line.split(": ")
        if rest.isnumeric():
            monkeys[name] = float(rest)
        else:
            monkeys[name] = rest.split(" ")
    # Now it is either a number or list of monkey, operator, monkey
    res = get_number("root")
    return res


def get_target():
    monkeys["humn"] = None
    try:
        target = get_number(monkeys["root"][0])
        other_name = monkeys["root"][2]
    except TypeError:
        target = get_number(monkeys["root"][2])
        other_name = monkeys["root"][0]
    return target, other_name


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    global monkeys
    for line in input_data:
        name, rest = line.split(": ")
        if rest.isnumeric():
            monkeys[name] = float(rest)
        else:
            monkeys[name] = rest.split(" ")

    # Instead of iterating one by one -> do a binary search
    # assumption: numbers are monotonically increasing
    # for that we need to know the other number of the computable child
    target, target_name = get_target()
    low = 0
    high = float(1_000_000_000_000)
    num = (low + high) // 2
    monkeys["humn"] = num
    while (other_num := get_number(target_name)) != target:
        # somehow other_num is negative for big numbers...
        if other_num < target:
            low = num
        else:
            high = num

        num = (low + high) // 2
        monkeys["humn"] = num
        print(num, other_num, target, low, high)

    return num


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 152

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 301

    result = part_2("input.txt")
    print(result)

from pathlib import Path
from typing import Any, Dict

monkeys: Dict[str, Any] = {}


def get_number(monkey: str) -> int:
    if isinstance(monkeys[monkey], int):
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
            monkeys[name] = int(rest)
        else:
            monkeys[name] = rest.split(" ")
    # Now it is either a number or list of monkey, operator, monkey
    res = get_number("root")
    return res


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


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

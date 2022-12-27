from pathlib import Path


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    all_numbers = []
    for snafu in input_data:
        all_numbers.append(snafu2decimal(snafu))

    decimal_num = sum(all_numbers)
    new_snafu = decimal2snafu(decimal_num)
    return sum(all_numbers), new_snafu


def snafu2decimal(snafu: str) -> int:
    new_number = []
    for letter in snafu:
        match letter:
            case "2":
                new_number.append(2)
            case "1":
                new_number.append(1)
            case "0":
                new_number.append(0)
            case "-":
                new_number.append(-1)
            case "=":
                new_number.append(-2)
        for i, old_num in enumerate(new_number[:-1]):
            new_number[i] = old_num * 5
    return sum(new_number)


def decimal2snafu(num: int) -> str:
    # Taken from https://old.reddit.com/r/adventofcode/comments/zur1an/2022_day_25_solutions/j1l08w6/
    # Why is this working?!
    if num != 0:
        # Get divisor and rest (modulo)
        div, rest = divmod(num + 2, 5)
        return decimal2snafu(div) + "=-012"[rest]
    else:
        return ""


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex, snafu = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 4890
    assert snafu == "2=-1=0"

    result, snafu = part_1("input.txt")
    print(result, snafu)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 1337

    result = part_2("input.txt")
    print(result)

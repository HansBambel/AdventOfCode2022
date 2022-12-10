from pathlib import Path


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    cycles = 1
    x = 1

    x_values = [x]

    for line in input_data:
        cycles += 1
        x_values.append(x)
        if line.startswith("addx"):
            _, num = line.split(" ")
            num = int(num)
            cycles += 1
            x_values.append(x)
            x += num

    signal_strength = [x * i for i, x in enumerate(x_values) if i == 20 or (i - 20) % 40 == 0]
    print(signal_strength)
    print(sum(signal_strength))

    return sum(signal_strength)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    cycles = 1
    x = 1
    current_line = "#"
    for line in input_data:
        current_line = draw_crt(cycles, x, current_line)
        cycles += 1
        if line.startswith("addx"):
            _, num = line.split(" ")
            num = int(num)
            x += num
            current_line = draw_crt(cycles, x, current_line)
            cycles += 1


def draw_crt(cycle: int, x: int, current_line: str):
    crt_row = cycle % 40
    if x - 1 <= crt_row <= x + 1:
        current_line += "#"
    else:
        current_line += " "
    if len(current_line) == 40:
        print(current_line)
        return ""
    return current_line


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 13140

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    # assert result == 1337

    result = part_2("input.txt")
    print(result)

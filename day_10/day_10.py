from pathlib import Path


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    cycles = 0
    x = 1

    sum_cycle_x = []

    for line in input_data:
        if line.startswith("noop"):
            cycles += 1
            if check_cycle(cycles):
                sum_cycle_x.append(cycles * x)
        else:
            _, num = line.split(" ")
            num = int(num)
            cycles += 1
            if check_cycle(cycles):
                sum_cycle_x.append(cycles * x)
            cycles += 1
            if check_cycle(cycles):
                sum_cycle_x.append(cycles * x)
            x += num

    print(sum_cycle_x)
    return sum(sum_cycle_x)


def check_cycle(cycles):
    return cycles == 20 or (cycles - 20) % 40 == 0


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    cycles = 0
    x = 1
    current_line = ""
    for line in input_data:
        if line.startswith("noop"):
            cycles += 1
        else:
            _, num = line.split(" ")
            num = int(num)
            cycles += 1
            current_line = draw_crt(cycles, x, current_line)
            cycles += 1
            x += num

        current_line = draw_crt(cycles, x, current_line)


def draw_crt(cycle: int, x: int, current_line: str):
    crt_row = cycle % 40
    if x - 1 <= crt_row <= x + 1:
        current_line += "#"
    else:
        current_line += "."
    if cycle % 40 == 0:
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

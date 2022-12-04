from pathlib import Path


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    total = 0
    for line in input_data:
        elf1, elf2 = line.split(",")[0], line.split(",")[1]
        min_elf1, max_elf1 = int(elf1.split("-")[0]), int(elf1.split("-")[1])
        min_elf2, max_elf2 = int(elf2.split("-")[0]), int(elf2.split("-")[1])

        if min_elf1 <= min_elf2 and max_elf1 >= max_elf2:
            total += 1
        elif min_elf2 <= min_elf1 and max_elf2 >= max_elf1:
            total += 1

    return total


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    total = 0
    for line in input_data:
        elf1, elf2 = line.split(",")[0], line.split(",")[1]
        min_elf1, max_elf1 = int(elf1.split("-")[0]), int(elf1.split("-")[1])
        min_elf2, max_elf2 = int(elf2.split("-")[0]), int(elf2.split("-")[1])

        if not (min_elf2 > max_elf1 or min_elf1 > max_elf2):
            total += 1

    return total


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 2

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 4

    result = part_2("input.txt")
    print(result)

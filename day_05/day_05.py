from pathlib import Path


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    prep, instr = data_file.split("\n\n")[0], data_file.split("\n\n")[1]
    stacks = [[] for _ in range(int(prep[-1][-1]))]
    prep = prep.split("\n")[:-1]
    instr = instr.split("\n")
    for line in prep:
        for stack in range(1, len(line), 4):
            if line[stack] != " ":
                stacks[(stack - 1) // 4].append(line[stack])

    for line in instr:
        number = int(line.split()[1])
        from_stack = int(line.split()[3]) - 1
        to_stack = int(line.split()[5]) - 1
        [stacks[to_stack].insert(0, stacks[from_stack].pop(0)) for _ in range(number)]

    code = "".join([stack.pop(0) for stack in stacks])
    return code


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    prep, instr = data_file.split("\n\n")[0], data_file.split("\n\n")[1]
    stacks = [[] for _ in range(int(prep[-1][-1]))]
    prep = prep.split("\n")[:-1]
    instr = instr.split("\n")
    for line in prep:
        for stack in range(1, len(line), 4):
            if line[stack] != " ":
                stacks[(stack - 1) // 4].append(line[stack])

    for line in instr:
        number = int(line.split()[1])
        from_stack = int(line.split()[3]) - 1
        to_stack = int(line.split()[5]) - 1

        tmp_stack = [stacks[from_stack].pop(0) for _ in range(number)]
        [stacks[to_stack].insert(i, tmp_stack.pop(0)) for i in range(number)]

    code = "".join([stack.pop(0) for stack in stacks])
    return code


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == "CMZ"

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == "MCD"

    result = part_2("input.txt")
    print(result)

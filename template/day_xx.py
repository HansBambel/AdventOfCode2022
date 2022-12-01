from pathlib import Path


def part_1(input: str):
    pass


def part_2(input: str):
    pass


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    data_ex = Path(__file__).with_name("input_ex.txt").read_text()
    result_ex = part_1(data_ex)
    print(result_ex)
    assert result_ex == 1337

    data = Path(__file__).with_name("input.txt").read_text()
    result = part_1(data)
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    data_ex = Path(__file__).with_name("input_ex.txt").read_text()
    result = part_2(data_ex)
    print(result)
    assert result == 1337

    data = Path(__file__).with_name("input.txt").read_text()
    result = part_2(data)
    print(result)

from pathlib import Path

OUTCOME = {"A X": 3, "A Y": 6, "A Z": 0, "B X": 0, "B Y": 3, "B Z": 6, "C X": 6, "C Y": 0, "C Z": 3}
POINTS_SHAPE = {"X": 1, "Y": 2, "Z": 3}

PART_2_WIN = {"X": 0, "Y": 3, "Z": 6}
PART_2_SHAPE = {
    "A X": "Z",
    "A Y": "X",
    "A Z": "Y",
    "B X": "X",
    "B Y": "Y",
    "B Z": "Z",
    "C X": "Y",
    "C Y": "Z",
    "C Z": "X",
}


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    points = 0
    for line in input_data:
        points += OUTCOME[line]
        points += POINTS_SHAPE[line[-1]]
    return points


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    points = 0
    for line in input_data:
        points += PART_2_WIN[line[-1]]
        points += POINTS_SHAPE[PART_2_SHAPE[line]]
    return points


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 15

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 12

    result = part_2("input.txt")
    print(result)

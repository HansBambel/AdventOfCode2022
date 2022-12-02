import enum
from pathlib import Path


class OpponentShape(str, enum.Enum):
    ROCK = "A"
    PAPER = "B"
    SCISSORS = "C"


class OwnShape(str, enum.Enum):
    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"


class Outcome(str, enum.Enum):
    WIN = "WIN"
    DRAW = "DRAW"
    LOSE = "LOSE"


class PointsOutcome(enum.IntEnum):
    WIN = 6
    DRAW = 3
    LOSE = 0


class PointsShape(enum.IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


OUTCOME_PART_1 = {
    f"{OpponentShape.ROCK} {OwnShape.ROCK}": Outcome.DRAW,
    f"{OpponentShape.ROCK} {OwnShape.PAPER}": Outcome.WIN,
    f"{OpponentShape.ROCK} {OwnShape.SCISSORS}": Outcome.LOSE,
    f"{OpponentShape.PAPER} {OwnShape.ROCK}": Outcome.LOSE,
    f"{OpponentShape.PAPER} {OwnShape.PAPER}": Outcome.DRAW,
    f"{OpponentShape.PAPER} {OwnShape.SCISSORS}": Outcome.WIN,
    f"{OpponentShape.SCISSORS} {OwnShape.ROCK}": Outcome.WIN,
    f"{OpponentShape.SCISSORS} {OwnShape.PAPER}": Outcome.LOSE,
    f"{OpponentShape.SCISSORS} {OwnShape.SCISSORS}": Outcome.DRAW,
}


class OutcomePart2(str, enum.Enum):
    LOSE = "X"
    DRAW = "Y"
    WIN = "Z"


TO_PLAY_PART_2 = {
    f"{OpponentShape.ROCK} {OutcomePart2.WIN}": OwnShape.PAPER,
    f"{OpponentShape.ROCK} {OutcomePart2.DRAW}": OwnShape.ROCK,
    f"{OpponentShape.ROCK} {OutcomePart2.LOSE}": OwnShape.SCISSORS,
    f"{OpponentShape.PAPER} {OutcomePart2.WIN}": OwnShape.SCISSORS,
    f"{OpponentShape.PAPER} {OutcomePart2.DRAW}": OwnShape.PAPER,
    f"{OpponentShape.PAPER} {OutcomePart2.LOSE}": OwnShape.ROCK,
    f"{OpponentShape.SCISSORS} {OutcomePart2.WIN}": OwnShape.ROCK,
    f"{OpponentShape.SCISSORS} {OutcomePart2.DRAW}": OwnShape.SCISSORS,
    f"{OpponentShape.SCISSORS} {OutcomePart2.LOSE}": OwnShape.PAPER,
}


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    points = 0
    for line in input_data:
        points += PointsOutcome[OUTCOME_PART_1[line].name].value
        points += PointsShape[OwnShape(line[-1]).name].value
    return points


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    points = 0
    for line in input_data:
        points += PointsOutcome[OutcomePart2(line[-1]).name].value
        points += PointsShape[TO_PLAY_PART_2[line].name].value
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

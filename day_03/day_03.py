from collections import Counter
from pathlib import Path


def points(letter: str) -> int:
    if letter.isupper():
        pts = ord(letter) - ord("A") + 1 + 26
    else:
        pts = ord(letter) - ord("a") + 1
    return pts


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    score = 0
    for line in input_data:
        first, second = line[: len(line) // 2], line[len(line) // 2 :]
        letters = {}
        for letter in first:
            letters[letter] = points(letter)

        for letter in second:
            if letters.get(letter) is not None:
                score += letters[letter]
                break
    return score


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    score = 0
    groups = []
    tmp = []
    for group, line in enumerate(input_data):
        tmp.append(line)
        if group % 3 == 2:
            groups.append(tmp)
            tmp = []

    for group in groups:
        letter_group = []
        for rucksack in group:
            letters_rucksack = []
            for letter in rucksack:
                if letter not in letters_rucksack:
                    letters_rucksack.append(letter)
            letter_group += letters_rucksack
        counter = Counter(letter_group)
        most_common_letter = counter.most_common()[0][0]
        score += points(most_common_letter)
    return score


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 157

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 70

    result = part_2("input.txt")
    print(result)

from pathlib import Path

import numpy as np


def calc_calories_and_elf(input_file: str):
    data_ex = Path(__file__).with_name(input_file).read_text()

    # Split into elves
    elves_carrying = data_ex.split("\n\n")
    # Split into calories per elf and convert to int
    elves_calories = [calories.split("\n") for calories in elves_carrying]
    elves_calories_int = [[int(cal) for cal in elf] for elf in elves_calories]

    cal_sum = [sum(elf) for elf in elves_calories_int]
    return cal_sum


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    cal_sum_ex = calc_calories_and_elf("input_ex.txt")
    print(cal_sum_ex)
    assert np.max(cal_sum_ex) == 24_000

    cal_sum = calc_calories_and_elf("input.txt")
    print(np.max(cal_sum))

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    assert sum(sorted(cal_sum_ex)[-3:]) == 45_000

    print(sum(sorted(cal_sum)[-3:]))

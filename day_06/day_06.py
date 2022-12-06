from pathlib import Path


def get_index(input_file: str, distinct_letters: int = 4) -> int:
    data_file = Path(__file__).with_name(input_file).read_text()
    i = distinct_letters
    while len(set(data_file[i - distinct_letters : i])) != distinct_letters:
        i += 1
    return i


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = get_index("input_ex.txt")
    assert get_index("input_ex.txt") == 5
    assert get_index("input_ex2.txt") == 6
    assert get_index("input_ex3.txt") == 10
    assert get_index("input_ex4.txt") == 11

    result = get_index("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = get_index("input.txt", distinct_letters=14)
    print(result)

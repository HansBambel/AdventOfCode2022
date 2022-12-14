from pathlib import Path


def get_layout(data_file):
    input_data = data_file.split("\n")
    rock_input = []
    for rocks in input_data:
        coords = [list(map(int, xy.split(","))) for xy in rocks.split(" -> ")]
        rock_input.append(coords)

    rock_layout = set()
    for rocks in rock_input:
        for i, second_pos in enumerate(rocks[1:]):
            first_pos = rocks[i]
            x_min, x_max = min(first_pos[0], second_pos[0]), max(first_pos[0], second_pos[0])
            y_min, y_max = min(first_pos[1], second_pos[1]), max(first_pos[1], second_pos[1])
            for x in range(x_min, x_max + 1, 1):
                for y in range(y_min, y_max + 1, 1):
                    rock_layout.add((x, y))
    return rock_layout


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    rock_layout = get_layout(data_file)

    # find min and max for creation of grid
    rocks_y = [y for _, y in rock_layout]
    rocks_max_y = max(rocks_y)

    sand_pos = set()
    sand_stopped = True
    while sand_stopped:
        # Move sand down
        new_sand, sand_stopped = sand_fall(rock_layout=rock_layout, rocks_max_y=rocks_max_y, sand_pos=sand_pos)

    return len(sand_pos)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    rock_layout = get_layout(data_file)

    # find min and max for creation of grid
    rocks_y = [y for _, y in rock_layout]
    rocks_max_y = max(rocks_y)

    # "infinite" here is 1000 :D
    for x in range(0, 1000 + 1, 1):
        rock_layout.add((x, rocks_max_y + 2))

    sand_pos = set()
    while True:
        # Move sand down
        new_sand, sand_stopped = sand_fall(rock_layout=rock_layout, rocks_max_y=rocks_max_y + 2, sand_pos=sand_pos)
        if sand_stopped and new_sand == (500, 0):
            break

    return len(sand_pos)


def sand_fall(rock_layout, rocks_max_y, sand_pos):
    """Let sand fall. If below is blocked, look below left then below right. If none are free -> sand is stopped."""
    new_sand = (500, 0)
    sand_stopped = False
    while new_sand[1] < rocks_max_y:
        x, y = new_sand
        if (x, y + 1) in rock_layout:
            # check to move left
            if (x - 1, y + 1) in rock_layout:
                # check to move right
                if (x + 1, y + 1) in rock_layout:
                    # Sand can't move anymore
                    sand_pos.add(new_sand)
                    rock_layout.add(new_sand)
                    sand_stopped = True
                    break
                else:
                    new_sand = (x + 1, y + 1)
            else:
                new_sand = (x - 1, y + 1)
        else:
            new_sand = (x, y + 1)
    return new_sand, sand_stopped


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 24

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 93

    result = part_2("input.txt")
    print(result)

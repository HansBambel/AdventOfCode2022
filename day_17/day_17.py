from pathlib import Path

from tqdm import tqdm


def part_1(input_file: str):
    movements = Path(__file__).with_name(input_file).read_text()
    correct = Path(__file__).with_name("correct heights").read_text().splitlines()
    chute_line = "......."
    # seven units wide
    chute = [chute_line] * 3

    rocks = [["####"], [".#.", "###", ".#."], ["###", "..#", "..#"], ["#", "#", "#", "#"], ["##", "##"]]

    height = 0
    units = 0
    for rock_count in tqdm(range(2022), desc="Rocks"):

        rock = rocks[rock_count % len(rocks)]
        # if rock_count == 15:
        #     break
        cur_x = 2
        cur_y = len(chute)
        # add the rock at the top
        for rock_part in rock:
            part = list(chute_line)
            part[2 : 2 + len(rock_part)] = rock_part
            chute.append("".join(part))
        rock_stopped = False
        while not rock_stopped:
            # check left/right movement

            movement = "right" if movements[units % len(movements)] == ">" else "left"
            # print(movement)
            # for l in chute[::-1]:
            #     print("|" + l + "|")
            # print("---------")

            units += 1
            free = True
            for i_r, rock_part in enumerate(rock):
                if movement == "right":
                    check_x = cur_x + 1 + rock_part.rfind("#")
                else:
                    # Find the first occurrence of a # in the rock part
                    check_x = cur_x - 1 + rock_part.find("#")
                # check if inside chute
                if not (0 <= check_x < 7):
                    free = False
                    break
                # Check for # overlap
                if chute[cur_y + i_r][check_x] == "#":
                    free = False
                    break
            if free:
                cur_x += 1 if movement == "right" else -1
                # Move the whole rock
                for i_r, rock_part in enumerate(rock):
                    line = list(chute[cur_y + i_r])
                    if movement == "left":
                        line[cur_x + rock_part.find("#")] = "#"
                        line[cur_x + 1 + rock_part.rfind("#")] = "."
                    else:
                        line[cur_x + rock_part.rfind("#")] = "#"
                        line[cur_x - 1 + rock_part.find("#")] = "."
                    chute[cur_y + i_r] = "".join(line)

            # check for move down
            free = True
            for i_r, rock_part in enumerate(rock):
                # Check for # overlap
                if cur_y <= 0:
                    free = False
                    break

                """
                    .......
                    ....#..
                    ...###.
                    ....#..
                    ..##...
                """

                line = list(chute[cur_y + i_r - 1])  # line below
                for i, p in enumerate(line[cur_x : cur_x + len(rock_part)]):
                    if i_r > 0:
                        if rock[i_r - 1][i] == "#":
                            break
                    if rock_part[i] == "#" and p == "#":
                        free = False
                        break
                if not free:
                    break
            if free:
                # move rock down
                for i_r, rock_part in enumerate(rock):
                    line_before = list(chute[cur_y + i_r])
                    line = list(chute[cur_y + i_r - 1])
                    for i, _ in enumerate(line[cur_x : cur_x + len(rock_part)]):
                        if rock_part[i] == "#":
                            line[cur_x + i] = "#"
                            # remove the previous
                            line_before[cur_x + i] = "."
                    chute[cur_y + i_r - 1] = "".join(line)
                    chute[cur_y + i_r] = "".join(line_before)

            else:
                rock_stopped = True
            cur_y -= 1

        # Remove the top
        while "".join(chute[-4:]).count("#") == 0:
            chute.pop(-1)
        while "".join(chute[-3:]).count("#") > 0:
            # add a line
            chute.append(chute_line)

        height = len(chute) - 3
        # print(rock_count, height, correct[rock_count])
        # if rock_count == 20:
        #     print("################################################################")
        #     pass
        # if rock_count ==22:
        #     break
        # if rock_count == 50:
        #     break

    return height


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 3068

    result = part_1("input.txt")
    assert result > 3098, result
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 1337

    result = part_2("input.txt")
    print(result)

from pathlib import Path


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    north = [(-1, 0), (-1, 1), (-1, -1)]
    south = [(+1, 0), (+1, 1), (+1, -1)]
    west = [(0, -1), (-1, -1), (+1, -1)]
    east = [(0, +1), (-1, +1), (+1, +1)]
    directions = [north, south, west, east]
    elves = set()
    for row, line in enumerate(input_data):
        for column, char in enumerate(line):
            if char == "#":
                elves.add((row, column))

    for i in range(10):
        first_dir = i % len(directions)
        wants_to_move = {}
        # first half: check for possible movement
        for elf_pos in elves:
            # N,S,W,E
            has_neighbor = False
            for coarse_dir_i in range(len(directions)):
                coarse_dir = directions[(first_dir + coarse_dir_i) % len(directions)]
                has_elf = [(elf_pos[0] + direction[0], elf_pos[1] + direction[1]) in elves for direction in coarse_dir]
                if any(has_elf):
                    has_neighbor = True
                    continue
                else:
                    if wants_to_move.get(elf_pos, None) is None:
                        wants_to_move[elf_pos] = (elf_pos[0] + coarse_dir[0][0], elf_pos[1] + coarse_dir[0][1])
            if not has_neighbor:
                wants_to_move.pop(elf_pos)

        # second half: do the move IF NO OTHER elf want to move there
        clean_moves = {}
        for elf_pos, new_pos in wants_to_move.items():
            if new_pos in clean_moves.values():
                # inefficient... remove the move that land on the same spot
                clean_moves = {k: v for k, v in clean_moves.items() if v != new_pos}
            else:
                clean_moves[elf_pos] = new_pos
        for elf_pos, new_pos in clean_moves.items():
            elves.remove(elf_pos)
            elves.add(new_pos)

        # PRINT
        # print(f"After ROUND {i+1}")
        # cave_max_y = max([y for y, _ in elves])
        # cave_min_y = min([y for y, _ in elves])
        # cave_max_x = max([x for _, x in elves])
        # cave_min_x = min([x for _, x in elves])
        # for y in range(cave_max_y-cave_min_y+1):
        #     for x in range(cave_max_x-cave_min_x+1):
        #         print("#" if (y+cave_min_y, x+cave_min_x) in elves else ".", end="")
        #     print()
        # print()

    # Get the max rectangle and count the fields
    min_y = min([y for y, _ in elves])
    max_y = max([y for y, _ in elves])
    min_x = min([x for _, x in elves])
    max_x = max([x for _, x in elves])

    tiles = (max_y - min_y + 1) * (max_x - min_x + 1)
    free_tiles = tiles - len(elves)
    return free_tiles


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    # result_ex2 = part_1("input_ex2.txt")
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 110

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 20

    result = part_2("input.txt")
    print(result)

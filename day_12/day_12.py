from pathlib import Path
from typing import Tuple

import numpy as np

from utils import bfs

neighbors = [(-1, 0), (+1, 0), (0, -1), (0, +1)]


def find_way(grid, costs, visited, start_pos: Tuple[int, int], end_pos=None):
    """Dijkstra"""
    pos = start_pos
    # For part 2 we went greedy -> can stop after the first vertex is found
    while (not any(visited[grid == 26])) if end_pos is None else (not visited[end_pos]):

        y, x = pos
        neighbor_coords = [
            (y + n_y, x + n_x)
            for n_y, n_x in neighbors
            if (0 <= y + n_y < grid.shape[0]) and (0 <= x + n_x < grid.shape[1]) and (not visited[(y + n_y, x + n_x)])
        ]

        visited[y, x] = True
        for n_coord in neighbor_coords:
            # increase costs
            if (grid[n_coord] - grid[pos]) <= 1:
                alt = costs[pos] + 1
            else:
                alt = np.inf
            if alt < costs[n_coord]:
                costs[n_coord] = alt

        # expand most promising node
        most_promising_node = np.unravel_index(np.argmin(np.where(~visited, costs, np.inf), axis=None), costs.shape)
        pos = most_promising_node


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    grid = np.ones((len(input_data), len(input_data[0])))
    start_y, start_x = 0, 0
    final_y, final_x = 0, 0

    for y, line in enumerate(input_data):
        for x, letter in enumerate(line):
            grid[y, x] = (ord(letter) - ord("a") + 1) if letter.islower() else 0 if letter == "S" else 27
            if letter == "S":
                start_y, start_x = y, x
            if letter == "E":
                final_y, final_x = y, x

    costs = np.ones(shape=grid.shape) * np.inf
    visited = np.zeros(shape=grid.shape, dtype=bool)
    # print(grid)
    costs[start_y, start_x] = 0

    # costs, path = bfs(grid, (start_y, start_x))

    find_way(grid=grid, costs=costs, visited=visited, start_pos=(start_y, start_x), end_pos=(final_y, final_x))
    # print(costs)
    return costs[final_y, final_x]


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    grid = np.ones((len(input_data), len(input_data[0])))
    final_y, final_x = 0, 0

    for y, line in enumerate(input_data):
        for x, letter in enumerate(line):
            grid[y, x] = (ord(letter) - ord("a") + 1) if letter.islower() else 1 if letter == "S" else 27
            if letter == "E":
                final_y, final_x = y, x

    # inverse the search
    grid = 27 - grid
    costs = np.ones(shape=grid.shape) * np.inf
    visited = np.zeros(shape=grid.shape, dtype=bool)
    # print(grid)
    costs[final_y, final_x] = 0

    find_way(grid=grid, costs=costs, visited=visited, start_pos=(final_y, final_x))
    # print(costs)
    return min(costs[grid == 26])


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 31

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 29

    result = part_2("input.txt")
    print(result)

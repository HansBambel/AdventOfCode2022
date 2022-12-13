from pathlib import Path
from queue import PriorityQueue
from typing import Tuple

import numpy as np

from utils import neighbors


def dijkstra(grid, start_pos: Tuple[int, int]):
    """Shortest path between paths."""
    prev = {}
    dist = np.ones(shape=grid.shape) * np.inf
    seen = np.zeros(shape=grid.shape, dtype=bool)
    dist[start_pos] = 0
    q = PriorityQueue()
    q.put((0, start_pos))

    while not q.empty():
        prio, cur_pos = q.get()
        seen[cur_pos] = True
        current_y, current_x = cur_pos
        new_neighbors = [
            (current_y + n_y, current_x + n_x)
            for n_y, n_x in neighbors
            if (0 <= current_y + n_y < grid.shape[0])
            and (0 <= current_x + n_x < grid.shape[1])
            and (not seen[(current_y + n_y, current_x + n_x)])
            # This filters out neighbors that are more than 1 higher than the current one
            and grid[(current_y + n_y, current_x + n_x)] - 1 <= grid[cur_pos]
        ]
        for pos in new_neighbors:
            # Calc new costs (would use grid[current_y, current_x] instead of +1)
            # alt = dist[cur_pos] + grid[pos]
            alt = dist[cur_pos] + 1

            if alt < dist[pos]:
                dist[pos] = alt
                prev[pos] = cur_pos
                q.put((alt, pos))
    return dist, prev


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

    costs, path = dijkstra(grid, (start_y, start_x))

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

    costs, path = dijkstra(grid, (final_y, final_x))

    # Find the minimum where the start values was 26
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

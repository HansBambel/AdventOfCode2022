import re
from pathlib import Path
from typing import Tuple

import numpy as np

from utils import neighbors


def add_manhatten_dist(pos: Tuple[int, int], dist: int, impossible_beacons: set):
    """Add all positions in manhatten distance by adding all neighbors and calling it recursively."""
    if dist < 0:
        return
    impossible_beacons.add(pos)
    for yn, xn in neighbors:
        add_manhatten_dist((pos[0] + yn, pos[1] + xn), dist - 1, impossible_beacons)


def part_1(input_file: str, row=10):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    sensors = []
    beacons = []
    for line in input_data:
        sensor, beacon = line.split(": ")
        sensor = list(map(int, re.findall(r"x=(-?\d+), y=(-?\d+)", sensor)[0]))
        beacon = list(map(int, re.findall(r"x=(-?\d+), y=(-?\d+)", beacon)[0]))
        sensors.append(tuple(sensor))
        beacons.append(tuple(beacon))

    x_pos = [pos[0] for pos in sensors] + [pos[0] for pos in beacons]
    y_pos = [pos[1] for pos in sensors] + [pos[1] for pos in beacons]
    min_x, max_x = min(x_pos), max(x_pos)
    min_y, max_y = min(y_pos), max(y_pos)

    # possible_beacons = np.zeros((max_y-max_y, max_x-min_x), dtype=bool)
    impossible_beacons = set(sensors)
    for sen, beac in zip(sensors, beacons):
        # Manhatten distance
        dist = abs(sen[0] - beac[0]) + abs(sen[1] - beac[1])
        # disable all points in possible_beacons from the sensor
        add_manhatten_dist(sen, dist, impossible_beacons)

    # Need to remove the found beacons!
    [impossible_beacons.discard(pos) for pos in beacons]
    result = sum([1 for x, y in impossible_beacons if y == row])
    return result


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt", row=10)
    print(result_ex)
    assert result_ex == 26

    result = part_1("input.txt", row=2000000)
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 1337

    result = part_2("input.txt")
    print(result)

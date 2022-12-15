import re
from collections import Counter
from pathlib import Path
from typing import Tuple

from tqdm import tqdm

from utils import neighbors


def add_manhatten_dist_rec(pos: Tuple[int, int], dist: int, impossible_beacons: set):
    """Add all positions in manhatten distance by adding all neighbors and calling it recursively."""
    if dist < 0:
        return
    impossible_beacons.add(pos)
    for xn, yn in neighbors:
        add_manhatten_dist_rec((pos[0] + xn, pos[1] + yn), dist - 1, impossible_beacons)


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

    impossible_beacons = set()
    for sen, beac in zip(sensors, beacons):
        # Manhatten distance
        dist = abs(sen[0] - beac[0]) + abs(sen[1] - beac[1])
        # disable all points in possible_beacons from the sensor
        if row not in range(sen[1] - dist, sen[1] + dist):
            continue

        """
        L1 = Manhatten distance = 3
        Interested row = 2
        on_row is the number of x values to the left and right of S that are reached
        on_row is the L1 - abs(Sy - interested row) -> 3 - abs(1-2) = 2
        --> two to the left and two to the right of S
            0 ..#####..
            1 .###S###.
        ->  2 ..B####..
            3 ...###...
            4 ....#....
            5 .........
            6 .........
        """
        # calc which ones are on the row and add them to the set
        on_row = dist - abs(sen[1] - row)
        impossible_beacons.add((sen[0], row))
        for x in range(sen[0] - on_row, sen[0] + on_row, 1):
            impossible_beacons.add((x, row))

    # Need to remove the found beacons!
    [impossible_beacons.discard(pos) for pos in beacons]
    # Magical + 1 error ?
    result = len(impossible_beacons)
    return result + 1


def part_2(input_file: str, max_pos=20):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    coords = [list(map(int, re.findall(r"(-?\d+)", line))) for line in input_data]

    """
    Idea: get the outer range+1 of the sensors outer range, remove those that are within the previous possible spaces
    """
    previous_ranges = []
    possible_beacon_spots = Counter()
    for sx, sy, bx, by in tqdm(coords, desc="Adding"):
        # Manhatten distance
        sensor, beac = (sx, sy), (bx, by)
        dist_cur = l1_dist(sensor, beac)

        rim_points = get_rim_edge(sensor, dist_cur, max_pos=max_pos)
        # Add edges to counter
        possible_beacon_spots.update(rim_points)

        previous_ranges.append((sensor, dist_cur))

    # Check these points that are inside the sensors ranges
    # when there is one point that is not covered by sensors -> break
    for pos, _ in tqdm(possible_beacon_spots.most_common(), desc="Checking"):
        is_covered = False
        for prev_sensor, sensor_range in previous_ranges:
            if l1_dist(prev_sensor, pos) <= sensor_range:
                is_covered = True
                break
        if not is_covered:
            break

    print(pos)
    return pos[0] * 4_000_000 + pos[1]


def l1_dist(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_rim_edge(pos: Tuple[int, int], dist: int, max_pos: int) -> set[Tuple[int, int]]:
    """Only add those that are still inside the field."""
    rim_points = set()
    for i in range(dist + 1):
        inverted = dist + 1 - i
        for x, y in [
            (pos[0] - i, pos[1] + inverted),
            (pos[0] - i, pos[1] - inverted),
            (pos[0] + i, pos[1] + inverted),
            (pos[0] + i, pos[1] - inverted),
        ]:
            if (0 <= x < max_pos) and (0 <= y < max_pos):
                rim_points.add((x, y))

    return rim_points


if __name__ == "__main__":
    # print("#" * 10 + " Part 1 " + "#" * 10)
    # result_ex = part_1("input_ex.txt", row=10)
    # print(result_ex)
    # assert result_ex == 26
    #
    # result = part_1("input.txt", row=2000000)
    # print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt", max_pos=20)
    print(result)
    assert result == 56000011

    result = part_2("input.txt", max_pos=4_000_000)
    print(result)

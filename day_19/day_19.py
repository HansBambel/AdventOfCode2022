import re
import sys
from functools import lru_cache, partial
from pathlib import Path
from typing import Tuple

sys.setrecursionlimit(1500)


@lru_cache(maxsize=None)
def decide(
    minutes: int,
    ore_robot_costs: int,
    clay_robot_costs: int,
    obsidian_robot_costs: Tuple[int, int],
    geode_robot_costs: Tuple[int, int],
    robots: Tuple[int, int, int, int],
    ore: int,
    clay: int,
    obsidian: int,
    geode: int,
):
    """Given the current situation, what is the best thing to do to get the most geodes?
    Returns the number of geodes that can be extracted.
    """
    if minutes <= 0:
        return geode
    # add stuff from miners
    ore += robots[0]
    clay += robots[1]
    obsidian += robots[2]
    geode += robots[3]

    # print(minutes, ore, clay, obsidian, geode, " robots", robots)

    filled_decide = partial(
        decide,
        ore_robot_costs=ore_robot_costs,
        clay_robot_costs=clay_robot_costs,
        obsidian_robot_costs=obsidian_robot_costs,
        geode_robot_costs=geode_robot_costs,
    )

    max_ore_costs = max([ore_robot_costs, clay_robot_costs, obsidian_robot_costs[0], geode_robot_costs[0]])
    # decide what can be done and try all of them in order:
    nothing, buy_ore_robot, buy_clay_robot, buy_obsidian_robot, buy_geode_robot = 0, 0, 0, 0, 0
    # buy geode miner
    if ore >= geode_robot_costs[0] and obsidian >= geode_robot_costs[1]:
        buy_geode_robot = filled_decide(
            minutes=minutes - 1,
            robots=(robots[0], robots[1], robots[2], robots[3] + 1),
            ore=ore - geode_robot_costs[0],
            clay=clay,
            obsidian=obsidian - geode_robot_costs[1],
            geode=geode,
        )
    # buy obsidian miner
    if robots[3] < geode_robot_costs[1] and robots[2] * minutes + obsidian < minutes * geode_robot_costs[1]:
        if ore >= obsidian_robot_costs[0] and clay >= obsidian_robot_costs[1]:
            buy_obsidian_robot = filled_decide(
                minutes=minutes - 1,
                robots=(robots[0], robots[1], robots[2] + 1, robots[3]),
                ore=ore - obsidian_robot_costs[0],
                clay=clay - obsidian_robot_costs[1],
                obsidian=obsidian,
                geode=geode,
            )
    # buy clay miner
    if robots[2] < obsidian_robot_costs[1] and robots[1] * minutes + clay < minutes * obsidian_robot_costs[1]:
        if ore >= clay_robot_costs:
            buy_clay_robot = filled_decide(
                minutes=minutes - 1,
                robots=(robots[0], robots[1] + 1, robots[2], robots[3]),
                ore=ore - clay_robot_costs,
                clay=clay,
                obsidian=obsidian,
                geode=geode,
            )
    # buy ore miner
    # some heuristics for faster conversion:
    # - only add an ore miner if we can use that much or up in a single minute
    # - if we already have enough ore don't produce more than we can use up
    if robots[0] < max_ore_costs and robots[0] * minutes + ore < minutes * max_ore_costs:
        if ore >= ore_robot_costs:
            buy_ore_robot = filled_decide(
                minutes=minutes - 1,
                robots=(robots[0] + 1, robots[1], robots[2], robots[3]),
                ore=ore - ore_robot_costs,
                clay=clay,
                obsidian=obsidian,
                geode=geode,
            )
    # only when nothing else can be done do nothing
    # if sum([buy_ore_robot, buy_clay_robot, buy_obsidian_robot, buy_geode_robot]) == 0:
    nothing = filled_decide(minutes=minutes - 1, robots=robots, ore=ore, clay=clay, obsidian=obsidian, geode=geode)

    most_geodes = max([nothing, buy_ore_robot, buy_clay_robot, buy_obsidian_robot, buy_geode_robot])
    # print([nothing, buy_ore_robot, buy_clay_robot, buy_obsidian_robot, buy_geode_robot])
    return most_geodes


def part_1(input_file: str, minutes=24):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")
    # Blueprint ID, ore costs (ore), clay costs (ore), obsidian costs (ore, clay), geode costs (ore obsidian)
    bb = [list(map(int, re.findall(r"\d+", line))) for line in input_data]

    geodes = {}
    for blueprint in bb:
        geodes[blueprint[0]] = decide(
            minutes,
            ore_robot_costs=blueprint[1],
            clay_robot_costs=blueprint[2],
            obsidian_robot_costs=(blueprint[3], blueprint[4]),
            geode_robot_costs=(blueprint[5], blueprint[6]),
            robots=(1, 0, 0, 0),
            ore=0,
            clay=0,
            obsidian=0,
            geode=0,
        )
        break
    # geodes = {blueprint[0]: decide(minutes,
    #            ore_robot_costs=blueprint[1],
    #            clay_robot_costs=blueprint[2],
    #            obsidian_robot_costs=(blueprint[3], blueprint[4]),
    #            geode_robot_costs=(blueprint[5], blueprint[6]),
    #            robots=(1,0,0,0),
    #            ore=0,
    #            clay=0,
    #            obsidian=0,
    #            geode=0,
    #            ) for blueprint in bb}
    print(geodes)
    quality_level = {bb_id * coll_geodes for bb_id, coll_geodes in geodes.items()}

    return sum(quality_level)


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 33

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 1337

    result = part_2("input.txt")
    print(result)

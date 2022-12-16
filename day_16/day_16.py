import re
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from queue import PriorityQueue
from typing import Dict, Tuple

import numpy as np

graph = {}


def dijkstra(graph: Dict, start_pos: str):
    """Shortest path between paths. Template that can be used and adapted."""
    prev: Dict[str, str] = {}
    dist: Dict[str, int] = defaultdict(lambda: np.inf)
    seen = set()

    q = PriorityQueue()
    q.put((0, start_pos, graph[start_pos]))

    dist[start_pos] = 0

    while not q.empty():
        prio, valve, (flow, conn_valves) = q.get()
        seen.add(valve)

        for pos in conn_valves:
            # Calc new costs (would use grid[current_y, current_x] instead of +1)
            alt = dist[valve] + 1
            # alt = dist[cur_pos] + 1

            if alt < dist[pos]:
                dist[pos] = alt
                prev[pos] = valve
                q.put((alt, pos, graph[pos]))
    return dist, prev


@lru_cache(maxsize=None)
def check_open_valves(opened: Tuple, cur_valve, minutes: int) -> int:
    global graph
    if minutes <= 0:
        return 0
    best_flow = 0

    for conn_valve in graph[cur_valve][1]:
        # open the valve and calc the flow resulting from this
        # sort it to have a better caching
        new_opened = tuple(sorted(opened + (cur_valve,)))
        new_flow = graph[cur_valve][0] * (minutes - 1)
        if cur_valve not in opened:
            # speed-up: no need to open the valve if it does not have a flow_rate
            if new_flow != 0:
                # The valve was opened and then we move
                remaining_flow_open = check_open_valves(new_opened, conn_valve, minutes - 2)
                best_flow = max(best_flow, new_flow + remaining_flow_open)

        remaining_flow_move = check_open_valves(opened, conn_valve, minutes - 1)
        best_flow = max(best_flow, remaining_flow_move)

    return best_flow


def part_1(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")

    valves = {}
    for line in input_data:
        valve, connections = line.split(";")
        found = re.findall(r"Valve (\w+).*=(\d+)", valve)[0]
        valve, flow = found[0], int(found[1])
        connections = re.findall(r"([A-Z]{2})", connections)
        valves[valve] = (flow, connections)

    global graph
    graph = valves
    # Add the valves that have flow rate 0 to be open already
    opened = {valve for valve, (flow, _) in graph.items() if flow == 0}
    highest_flow = check_open_valves(tuple(opened), "AA", minutes=30)

    return highest_flow


def part_2(input_file: str):
    data_file = Path(__file__).with_name(input_file).read_text()
    input_data = data_file.split("\n")


if __name__ == "__main__":
    print("#" * 10 + " Part 1 " + "#" * 10)
    result_ex = part_1("input_ex.txt")
    print(result_ex)
    assert result_ex == 1651
    # Clear cache!
    check_open_valves.cache_clear()

    result = part_1("input.txt")
    print(result)

    # #### Part 2 ####
    print("#" * 10 + " Part 2 " + "#" * 10)
    result = part_2("input_ex.txt")
    print(result)
    assert result == 1337
    # Clear cache!
    check_open_valves.cache_clear()

    result = part_2("input.txt")
    print(result)

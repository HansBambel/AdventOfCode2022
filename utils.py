from queue import LifoQueue, PriorityQueue, Queue
from typing import Dict, Tuple

import numpy as np

neighbors = [(-1, 0), (+1, 0), (0, -1), (0, +1)]


def dijkstra(grid: np.array, start_pos: Tuple[int, int]) -> Tuple[np.array, Dict[Tuple[int, int], Tuple[int, int]]]:
    """Shortest path between paths. Template that can be used and adapted."""
    prev: Dict[Tuple[int, int], Tuple[int, int]] = {}
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
            # and grid[(current_y + n_y, current_x + n_x)] - 1 <= grid[cur_pos]
        ]
        for pos in new_neighbors:
            # Calc new costs (would use grid[current_y, current_x] instead of +1)
            alt = dist[cur_pos] + grid[pos]
            # alt = dist[cur_pos] + 1

            if alt < dist[pos]:
                dist[pos] = alt
                prev[pos] = cur_pos
                q.put((alt, pos))
    return dist, prev


def get_path(graph: Dict[Tuple[int, int], Tuple[int, int]], goal_pos: Tuple[int, int]):
    """Get the path from the start to the goal."""
    path = []
    cur_pos = goal_pos
    while graph.get(cur_pos, None):
        path.append(cur_pos)
        cur_pos = graph[cur_pos]
    return path[::-1]


def search_path(
    grid: np.array,
    start_pos: Tuple[int, int],
    goal_pos: Tuple[int, int],
    search_style: str = "bfs",
    use_costs: bool = False,
):
    """Find a path in the grid from the start_pos.
    Costs are by default single steps.
    :param grid: Numpy array with the costs for each step
    :param start_pos: Starting position
    :param goal_pos: Goal position
    :parameter search_style: can be either "bfs" (Breadth-first-search) or "dfs" (Depth-first-search)
    :parameter use_costs: Flag whether to use the costs from the grid, if False, a cost of 1 for every step is assumed
    """
    assert search_style in ["bfs", "dfs"]
    if search_style == "bfs":
        Q = Queue()
    else:
        Q = LifoQueue()

    seen = {start_pos}
    prev = {}
    Q.put(start_pos)
    while not Q.empty():
        cur_pos = Q.get()
        # Check for goal found
        if cur_pos == goal_pos:
            break

        current_y, current_x = cur_pos
        new_neighbors = [
            (current_y + n_y, current_x + n_x)
            for n_y, n_x in neighbors
            if (0 <= current_y + n_y < grid.shape[0])
            and (0 <= current_x + n_x < grid.shape[1])
            and (current_y + n_y, current_x + n_x) not in seen
            # This filters out neighbors that are more than 1 higher than the current one
            # and grid[(current_y + n_y, current_x + n_x)] - 1 <= grid[cur_pos]
        ]
        for pos in new_neighbors:
            seen.add(pos)
            prev[pos] = cur_pos
            Q.put(pos)

    path = get_path(prev, goal_pos=goal_pos)
    if use_costs:
        costs = sum([grid[pos] for pos in path])
    else:
        costs = len(path)
    return costs, path

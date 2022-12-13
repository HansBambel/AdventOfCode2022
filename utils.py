from queue import PriorityQueue
from typing import Tuple

import numpy as np

neighbors = [(-1, 0), (+1, 0), (0, -1), (0, +1)]


def dijkstra(grid, start_pos: Tuple[int, int]):
    """Shortest path between paths. Template that can be used and adapted."""
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

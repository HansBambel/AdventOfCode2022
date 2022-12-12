from collections import deque
from typing import Tuple

import numpy as np

neighbors = [(-1, 0), (+1, 0), (0, -1), (0, +1)]


def bfs(grid, start_pos: Tuple[int, int]):
    """Best first search? Not working properly though :("""
    q = deque([start_pos])
    prev = {}
    seen = np.zeros(shape=grid.shape, dtype=bool)
    dist = np.ones(shape=grid.shape) * np.inf
    dist[start_pos] = 0

    while len(q) > 0:
        cur_pos = q.popleft()
        seen[cur_pos] = True
        current_y, current_x = cur_pos
        new_neighbors = [
            (current_y + n_y, current_x + n_x)
            for n_y, n_x in neighbors
            if (0 <= current_y + n_y < grid.shape[0])
            and (0 <= current_x + n_x < grid.shape[1])
            and (not seen[(current_y + n_y, current_x + n_x)])
        ]
        for pos in new_neighbors:
            # Special condition: only allowed to go one up (but infinite down)
            if grid[pos] - grid[cur_pos] > 1:
                continue

            q.append(pos)
            # Calc new costs (would use grid[current_y, current_x] instead of +1)
            # alt = dist[cur_pos] + grid[pos]
            alt = dist[cur_pos] + 1
            if alt < dist[pos]:
                dist[pos] = alt
                prev[pos] = cur_pos
    return dist, prev

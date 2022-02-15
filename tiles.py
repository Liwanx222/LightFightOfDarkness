# coding:utf8

from typing import List

class Tile():
    def __init__(self, name:str, path:str, neigh_N=None, neigh_E=None, neigh_S=None, neigh_W=None) -> None:
        self._map_name = name
        self._map_path = path
        self._neighbor_north = neigh_N
        self._neighbor_est = neigh_E
        self._neighbor_south = neigh_S
        self._neighbor_west = neigh_W
    
    def get_name(self) -> str:
        return self._map_name
    
    def get_path(self) -> str:
        return self._map_path
    
    def get_north(self):
        return self._neighbor_north
    
    def get_est(self):
        return self._neighbor_est
    
    def get_south(self):
        return self._neighbor_south
    
    def get_west(self):
        return self._neighbor_west
    
    def get_neighbors(self) -> List:
        """Return a list containing this tile's neighbors (None if no neighbor).\n
        Exemple : [None, None, None, None] if no tile next to it."""
        neighbors = []
        neighbors.append(self._neighbor_north)
        neighbors.append(self._neighbor_est)
        neighbors.append(self._neighbor_south)
        neighbors.append(self._neighbor_west)
        return neighbors

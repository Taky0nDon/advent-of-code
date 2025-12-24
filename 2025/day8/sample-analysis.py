#! /home/mike/opt/Python-3.14.0/py
import re
from dataclasses import dataclass
from binary_tree import TrinaryTreeNode


@dataclass
class GlobalStats:
    split_count: int = 0
    paths: int = 0

class GraphNode:
    def __init__(self, val, line):
        self.val = val
        self.line = line
        self.links = set()

    def __eq__(self, other):
        return self.val == other.val and self.line == other.line

    def __hash__(self):
        return hash((self.val, self.line))

    def __repr__(self):
        return f"{self.val + 1}, {self.line}"

    def add_link(self, other_node):
        self.links.add(other_node)

    def get_links(self):
        return sorted(tuple(self.links), key= lambda x: x.val)

    def depth_first_search(self):
        def _dfs(node):
            neighbors = node.get_links()
            if not neighbors:
                stats.paths += 1
                return
            for neighbor in node.get_links():
                _dfs(neighbor)
        _dfs(self)


def get_next_position(char: str, x: int) -> tuple[int]:
    if char == "^":
        stats.split_count += 1
        if len(lines[0]) - 1 > x >= 1:
            return x - 1, x + 1
        if x == 0:
            return x + 1
        if x == len(lines[0]) - 1:
            return x - 1
    return x,


if __name__ == "__main__":
    stats = GlobalStats()

    with open("input") as f:
        data = f.read()
    lines = data.strip().split("\n")

    START = lines[0].index("S")
    head = GraphNode(START, 1)
    next_x = [head]
    for y, line in enumerate(lines[:-1]):
        beam_locations = next_x.copy()
        flat_list = []
        tmpx = list()
        for node in beam_locations:
            v = node.val
            next_ = get_next_position(lines[y+1][v], v)
            for pos in set(next_):
                new_node = GraphNode(pos, y+2)
                if new_node not in tmpx:
                    node.add_link(new_node)
                    tmpx.append(new_node)
                else:
                    node.add_link(next(filter(lambda n: n == new_node, tmpx), None))
        next_x = tmpx

    head.depth_first_search()
    print(f"splits: {stats.split_count}")
    print(stats.paths)

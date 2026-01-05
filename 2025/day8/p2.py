from graphnode import GraphNode


def get_input(path: str) -> str:
    with open(path) as f:
        cont = f.read()
    return cont


def transform_row(row: str, beams: list[int]) -> str:
    gen = (c if i not in beams or c == "^" else "|" for i, c in enumerate(row))
    return "".join(gen)


def get_timelines(root: GraphNode) -> int:
    print(f"I am {root}")
    if len(root.links) == 0:
        root.timelines = 1
        print(f"I am returning 1")
        return 1
    if root.timelines:
        print(f"About to return `{root.timelines}`")
        return root.timelines
    for node in root.links:
        print("I'm checking all my links")
        root.timelines += get_timelines(node)
    return root.timelines


def build_graph(rows: list[str]) -> GraphNode:
    global splits
    starting_column = rows[0].index("S") 
    root_value = 0, starting_column
    node_cache = {}

    root = GraphNode(root_value)
    curr = [root]
    beams = []

    for row in range(1, len(rows)):
        for node in curr:
            node_cache[node.val] = node
            node_row, col = node.val
            if rows[row][col] == "^":
                splits += 1
                left_pos = (row, col - 1)
                right_pos = (row, col + 1)
                node.links.add(GraphNode(left_pos))
                node.links.add(GraphNode(right_pos))
            else:
                node.links.add(GraphNode((row, col)))

            for other_node in node.links:
                beams.append(other_node)
        curr = list(set(beams))
        beams = []
    return root


PUZZLE = "input"
if __name__ == "__main__":
    print("reading data")
    data = get_input(PUZZLE)
    lines = data.split()
    beam_path = [transform_row(lines[0], [lines[0].index("S")])]
    num_rows = len(lines)

    splits = 0
    root = build_graph(lines)
    tl = get_timelines(root)

    print("splits: ", splits)
    print("timelines: ", tl)


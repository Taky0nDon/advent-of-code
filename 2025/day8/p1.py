from binary_tree import TrinaryTreeNode

def get_input(path: str) -> str:
    with open(path) as f:
        cont = f.read()
    return cont

def transform_row(row: str, beams: list[int]) -> str:
    gen = (c if i not in beams or c == "^" else "|" for i,c in enumerate(row))
    return "".join(gen)

def get_timelines(root: TrinaryTreeNode) -> int:
    print(f"checking node {root.val}")
    print(f"children: {root.left.val if root.left else None},\
            {root.right.val if root.right else None}")
    if root is None:
        print("Visiting null node (I don't think this should happen.")
        return 1
    if root.left is None and root.right is None:
        print("visiting terminal node, return 1")
        root.timelines = 1
        return root.timelines
    left_timelines = get_timelines(root.left)
    right_timelines = get_timelines(root.right)
    return root.timelines
    print("none of the above")

def build_graph(rows: list[str]) -> TrinaryTreeNode:
    global splits
    root_value = 0,rows[0].index("S")
    row_length = len(rows[0])
    num_rows = len(rows)
    visited = set()

    root = TrinaryTreeNode(root_value)
    visited.add(root)
    curr = [root]
    beams = []

    for row_index in range(1, num_rows):
        splits_encountered = set()
        for node in curr:
            if rows[row_index][node.val[1]] == "^":
                if node.val[1] not in splits_encountered:
                    splits_encountered.add(node.val[1])
                    splits += 1
                    left_candidate  = TrinaryTreeNode((row_index, node.val[1] - 1))
                    right_candidate  = TrinaryTreeNode((row_index, node.val[1] + 1))
                    if left_candidate in visited:
                        left_node = next(visited)
                        while left_node != TrinaryTreeNode((row_index, node.val[1] - 1)):
                            left_node = next(visted)
                        node.left = left_node
                    else:
                        node.left = left_candidate
                    if right_candidate in visited:
                        right_node = next(visited)
                        while right_node != TrinaryTreeNode((row_index, node.val[1] - 1)):
                            right_node = next(visted)
                        node.right = right_node
                    else:
                        node.right = right_candidate
                    visited.add(node.left)
                    visited.add(node.right)
                    beams.extend([node.left, node.right])
            else:
                beams.append(node)
        beam_path.append(transform_row(rows[row_index], [node.val[1] for node in beams]))
        curr = beams
        beams = []
    return root
    
PUZZLE = "five-splits.txt"
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
    final_routes = None
    print("routes: ", root.timelines)


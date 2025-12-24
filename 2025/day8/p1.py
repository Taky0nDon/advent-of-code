from binary_tree import BinaryTreeNode

def get_input(path: str) -> str:
    with open(path) as f:
        cont = f.read()
    return cont

PUZZLE = "input"
if __name__ == "__main__":
    print("reading data")
    data = get_input(PUZZLE)
    lines = data.split()
    num_lines = len(lines)

    start = lines[0].index("S")
    root = BinaryTreeNode(start)
    current_node = root
    position_history = []
    added_nodes = [root]
    splits = 0
    print("num ^: ", data.count("^"))
    print("line length: ", len(lines))
    exit()

    for i in range(1, num_lines - 1):
        print(f"Checking line {i} of {num_lines}")
        for node in added_nodes.copy():
            current_node = added_nodes.pop(0)
            if lines[i + 1][current_node.val] == "^":
                current_node.left = BinaryTreeNode(current_node.val - 1)
                current_node.right = BinaryTreeNode(current_node.val + 1)
                added_nodes.extend([current_node.left, current_node.right])
            else:
                added_nodes.append(current_node)

    print("splits: ", splits)
    final_routes = root.depth_first_search(0)
    print("routes: ", final_routes)


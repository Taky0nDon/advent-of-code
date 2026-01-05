class GraphNode:
    node_cache = {}
    def __new__(cls, *args, **kwargs):
        coordinates = args[0]
        print("in __new__")
        print(f"args: {args}, kwargs: {kwargs}")
        if coordinates in cls.node_cache:
            print(f"{coordinates} already exists!")
            return cls.node_cache[args[0]]
        print("point not graphed yet...")
        cls.node_cache[args[0]] = super().__new__(cls)
        return cls.node_cache[args[0]]

    def __init__(self, val):
        print("in __init__")
        self.val = val
        self.links = set()
        self.timelines = 0

    def __eq__(self, other):
        return self.val == other.val

    def __hash__(self):
        return hash(self.val)

    def __repr__(self):
        value = f"{self.val}"
        children = f"{" ".join([str(l.val) for l in self.links])}"
        return f"val: {value} links: {children}\n and I live at {id(self)}"

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


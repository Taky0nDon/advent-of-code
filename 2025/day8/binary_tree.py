class TrinaryTreeNode():
    routes = 0
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.right = right
        self.straight = None
        self.left = left

    def pre_order_traversal(self):
        if self.left is not None:
            self.left.pre_order_traversal()
        elif self.right is not None:
            self.right.pre_order_traversal()
        else:
            return

    def depth_first_search(self, routes, visited=[]):
        self.routes = routes
        if self.left is None and self.right is None:
            self.routes += 1
            return self.routes
        if self.left is not None:
            self.routes = self.left.depth_first_search(self.routes)
        if self.right is not None:
            self.routes = self.right.depth_first_search(self.routes)
        return self.routes

    def __repr__(self):
        print('hi')
        if self is None:
            return ""
        the_string = [f"{' '*30}{self.val}"]
        levels = 1
        while self.left is not None or self.right is not None:
            if self.left is None:
                lval = "None"
            else:
                lval = str(self.left.val)
            if self.right is None:
                rval = "None"
            else:
                rval = str(self.right.val)
            the_string.append(f"{' '*(30 - levels)}/ \\ ")
            the_string.append(f"{' '*(30 - len(lval+rval))}{lval}"
                              f"{' '*(3 * levels)}{rval}")
            the_string += self.left.__repr__()
            the_string += self.right.__repr__()
            levels += 1
        return "\n".join(the_string)
if __name__ == "__main__":
    # order of node printing: 9, 7, 5, 3, 2, 1, 2, 4, 6, 7
    print(f'{" "*8}9')
    print(f'{" "*6}7')
    print(f'{" "*4}5')
    print(f'{" "*2}3')
    print(f'{" "*0}1')
    print(f'{" "*2}2')
    print(f'{" "*4}4')
    print(f'{" "*6}6')
    print(f'{" "*8}8')



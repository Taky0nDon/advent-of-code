class DoublyLinkedNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def build_list(self, starter_node_val: int):
        d = DoublyLinkedNode(starter_node_val)
        n = d.val + 1
        f = d
        while n < 100:
            f.next = DoublyLinkedNode(n)
            f.next.prev = f
            f = f.next
            n += 1
        b = d
        n = d.val - 1
        while n >= 0:
            b.prev = DoublyLinkedNode(n)
            b.prev.next = b
            b = b.prev
            n -= 1
        b.prev = f
        f.next = b

        return d

if __name__ == "__main__":
    my_list = DoublyLinkedNode().build_list(50)
    print(my_list.val)
    for _ in range(50):
        my_list = my_list.next
    print(my_list.val)
    for _ in range(61):
        my_list = my_list.prev
    print(my_list.val)

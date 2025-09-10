m = 4
ID = 2 ** m

class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.successor = None
        self.finger = [None] * m

    def set_successor(self, successor):
        self.successor = successor

    def set_finger_table(self, nodes):
        for i in range(m):
            start = (self.id + 2 ** i) % ID
            self.finger[i] = self.find_successor(start, nodes)

    def find_successor(self, key, nodes):
        if self._in_range(key, self.id, self.successor.id):
            return self.successor
        next_node = self.closest_preceding_node(key)
        return next_node.find_successor(key, nodes) if next_node != self else self.successor

    def closest_preceding_node(self, key):
        for f in reversed(self.finger):
            if f and self._in_range(f.id, self.id, key):
                return f
        return self

    def _in_range(self, x, a, b):
        if a < b:
            return a < x <= b
        return x > a or x <= b

    def __repr__(self):
        return f"Node({self.id})"

def main():
    node_ids = [1, 3, 7, 10, 14]
    nodes = [Node(i) for i in node_ids]

    # Thiết lập successor và finger table
    for i, node in enumerate(nodes):
        node.set_successor(nodes[(i + 1) % len(nodes)])
    for node in nodes:
        node.set_finger_table(nodes)

    # Lookup key = 9 bắt đầu từ Node 1
    key = 9
    start_node = nodes[0]
    path = []

    def lookup(node, key):
        path.append(node.id)
        if node._in_range(key, node.id, node.successor.id):
            path.append(node.successor.id)
            return node.successor
        next_node = node.closest_preceding_node(key)
        return lookup(next_node, key) if next_node != node else node.successor

    responsible = lookup(start_node, key)

    print(f"Lookup key {key} từ Node {start_node.id}")
    print(f"Đường đi: {path}")
    print(f"Node {responsible.id} lưu trữ key {key}")

if __name__ == "__main__":
    main()

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        self.prev = None 
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.dict = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head 
        
    def get(self, key: int) -> int:
        if key not in self.dict: 
            return -1 
        node = self.dict[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            old_node = self.dict[key]
            self.remove(old_node)
        new_node = Node(key, value)
        self.dict[key] = new_node
        self.add(new_node)

        if len(self.dict) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dict[node_to_delete.key]

    def add(self, node):
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev 
# A linked list is made up of nodes, each of which contains a value and a pointer to the next node in the sequence


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# double linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

# circular linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data}'

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        head, ret = self.head, []
        while head:
            ret.append(str(head))
            head = head.next
        return '->'.join(ret)

    # Adds node to end of linked list in O(1)
    def add_to_head(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # Adds node to end of linked list in O(1)
    def add_to_tail(self, data):
        if not self.head:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
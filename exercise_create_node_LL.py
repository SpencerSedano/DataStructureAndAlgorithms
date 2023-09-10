class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        



ll = LinkedList(4)

print('Head:', ll.head.value)
print('Tail:', ll.tail.value)
print('Length:', ll.length)
                                                                                                                    
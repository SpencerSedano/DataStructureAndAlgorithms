class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def countNodes(head):
    count = 1
    current = head
    while current.next != None:
        current = current.next
        count += 1
    return count

nodeA = Node(6)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

print(countNodes(nodeA))
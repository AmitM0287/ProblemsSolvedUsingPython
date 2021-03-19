class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    linked_list = LinkedList()
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node4 = Node(7)
    linked_list.head = node1
    linked_list.head.next = node2
    node2.next = node3
    node3.next = node4
    linked_list.traverse()

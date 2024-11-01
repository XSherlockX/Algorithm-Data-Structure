class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def InsertAtIndex(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    return "Index out of range"
                current = current.next
            if current is None:
                return "Index out of range"
            new_node.next = current.next
            if current.next:
                current.next.prev = new_node
            current.next = new_node
            new_node.prev = current

    def InsertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def InsertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def UpdateNode(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for i in range(index - 1):
                if current is None:
                    return
                current = current.next
            if current is None:
                return
            new_node.next = current.next.next
            new_node.prev = current
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node

    def removeNodeAtIndex(self, index):
        if self.head is None or index < 0:
            return None
        current = self.head
        for i in range(index):
            if current is None:
                return None
            current = current.next
        if current is None:
            return None
        removed_data = current.data
        if current.prev is not None:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next is not None:
            current.next.prev = current.prev
        return removed_data

    def RemoveAtEnd(self):
        new_node = self.head
        if self.head is Node:
            return False
        while new_node.next.next != None:
            new_node = new_node.next
        new_node.next = None
        new_node.perv = new_node

    def RemoveNodeAtBegin(self):
        if self.head is None:
            raise Exception("The list is Empty")
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return data

    def SizeOfList(self):
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size

    def Concatenate(self, other_list):
        current = self.head
        while current.next:
            current = current.next
        current.next = other_list.head
        if other_list.head:
            other_list.head.prev = current

    def Invert(self):
        current = None
        temp = self.head
        while temp:
            current = temp
            temp.prev, temp.next = temp.next, temp.prev
            temp = temp.prev
        if current:
            self.head = current
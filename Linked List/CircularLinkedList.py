class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def InsertAtIndex(self, data, index):
        new_node = Node(data)
        if index == 0:
            if not self.head:
                new_node.next = new_node
                self.head = new_node
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = new_node
                new_node.next = self.head
                self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
                if current == self.head:
                    raise IndexError("Index out of range")
            new_node.next = current.next
            current.next = new_node

    def AddToEmpty(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node

    def AddToBegin(self, data):
        new_node = Node(data)
        if (self.head == None):
            return self.AddToEmpty(data)
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node


    def AddToEnd(self, data):
        new_node = Node(data)
        if (self.head == None):
            return self.AddToEmpty(data)
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def UpdateNode(self, data, index):
        if self.head is None:
            return False

        new_node = self.head
        count = 0
        while True:
            if count == index:
                new_node.data = data
                return
            new_node = new_node.next
            count = count + 1
            if new_node == self.head:
                break

    def RemoveAtIndex(self, index):
        if not self.head:
            return
        if index == 0:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
        else:
            count = 0
            current = self.head
            prev = None
            while True:
                prev = current
                current = current.next
                count += 1
                if count == index:
                    prev.next = current.next
                    current = None
                    break

    def RmeoveAtEnd(self):
        if self.head == None:
            return False
        elif self.head.next == self.head:
            self.head = None
        new_node = self.head
        while new_node.next.next != self.head:
            new_node = new_node.next
        new_node.next = self.head

    def RemoveNodeAtBegin(self):
        if self.head is None:
            return None
        temp = self.head
        data = temp.data
        if self.head.next == self.head:
            self.head = None
        else:
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
        return data

    def SizeOfList(self):
        if self.head is None:
            return 0
        count = 1
        current = self.head
        while current.next != self.head:
            current = current.next
            count += 1
        return count

    def Concatenate(self, other_linked_list):
        if self.head is None:
            self.head = other_linked_list.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = other_linked_list.head

    def Invert(self):
        if self.head is None:
            return
        prev = None
        current = self.head
        next_node = self.head.next
        while next_node != self.head:
            current.next = prev
            prev = current
            current = next_node
            next_node = next_node.next
        current.next = prev
        self.head.next = current
        self.head = current

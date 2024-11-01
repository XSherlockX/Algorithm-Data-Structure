class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def InsertAtIndex(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    raise IndexError("Index out of range")
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node           

        else:
            new_node.next = self.head
            self.head = new_node
            

    def InserAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node
        

    def UpdateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next
    
            if position == index :
                current_node.data = val
            else:
                return False
            
    def RemoveNodeAtIndex(self, index):
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            current_node_value = self.head
            self.head = self.head.next
            return current_node_value

        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
            
            if position+1 == index:
                current_node_value = current_node.next             
                current_node.next = current_node.next.next
                
                return current_node_value
                
            else:
                return False

    def RemoveNodeAtEnd(self):
        if self.head is None:
            return None
        if self.head.next is None:
            current_node_value = self.head
            self.head = None
            return current_node_value

        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        current_node_value = current_node.next
        current_node.next = None
        return current_node_value

    def RemoveNodeAtBegin(self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def sizeOfList(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next
        return size

    def concatenate(self, list2):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = list2.head
        else:
            self.head = list2.head

    def invert(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def Find(self, data):
        current_node = self.head
        position = 0
        if self.head.data == data:
            return 0
        if self.head is None:
            return

        while current_node.data == data:
            current_node = current_node.next
            position = position + 1
        return position

    def display(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next


# test :

obj = LinkedList()

obj.InsertAtIndex(0, 0)
obj.InsertAtIndex(1, 1)
obj.InsertAtIndex(2, 2)
obj.InsertAtIndex(3, 3)


obj.RemoveNodeAtEnd()

obj.RemoveNodeAtBegin()

obj.UpdateNode(85, 1)

obj.invert()
print(obj.Find(1))


obj.display()






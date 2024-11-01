import linked_list

class ArrayReplica:
    array = linked_list.LinkedList()

    def Insert(self, data, index):
        self.array.InsertAtIndex(data, index)

    def Delete(self, index):
        self.array.RemoveNodeAtIndex(index)

    def Find(self, data):
        self.array.Find(data)
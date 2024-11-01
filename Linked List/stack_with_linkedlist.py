import linked_list


class StackReplica:
    stack = linked_list.LinkedList()

    def push(self, data):
        self.stack.InserAtEnd(data)

    def display(self):
        self.stack.display()

    def pop(self):
        return self.stack.RemoveNodeAtEnd()

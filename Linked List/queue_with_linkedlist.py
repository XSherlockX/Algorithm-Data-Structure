import linked_list


class QueueReplica:
    queue = linked_list.LinkedList()

    def enqueue(self, data):
        self.queue.InserAtEnd(data)

    def dequeue(self):
        self.queue.RemoveNodeAtBegin()

    def first(self):
        return self.queue.head.data


class QueueReplica:
    counter = -1
    queue = list()

    def __init__(self, size):
        for i in range(size):
            self.queue.append(None)
            self.size = size

    def enqueue(self, value):
        if(self.counter == -1):
            self.counter += 1
            self.queue[self.counter] = value
        elif self.counter == self.size:
            self.is_full()
        else:
            self.counter += 1
            self.queue[self.counter] = value


    def dequeue(self):
        if self.counter != -1:
            for i in range(self.size - 1):
                self.queue[i] = self.queue[i + 1]
        else:
            self.is_empty()

    def peek(self):
        return self.queue[0]
    
    

    def is_empty(self):
        if self.counter == -1:
            return True
        else:
            return False


    def is_full(self):
        if self.counter == self.size:
            return True
        else:
            return False

    def reverse(self):
        start = 0
        temp = self.size
        end = temp - 1

        while start < end:
            self.queue[start], self.queue[end], = self.queue[end], self.queue[start]
            start += 1
            end -= 1

        return self.queue



class Queue:
    def __init__(self, limit=10):
        self.queue = []
        self.front = None
        self.rear = None
        self.limit = limit

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        if len(self.queue) >= self.limit:
            return print("queue overflow")
        else:
            self.queue.append(data)

        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = len(self.queue) - 1

    def dequeue(self):
        if self.isEmpty():
            return print("queue is empty")

        else:
            self.queue.pop(0)
            if len(self.queue) == 0:
                self.front = self.rear = None
            else:
                self.rear = len(self.queue) - 1

    def peek(self):
        return self.front


class DoubleEndedQueue(Queue):
    def __init__(self, limit=10):
        super().__init__(limit)

    def enqueue_front(self, data):
        if len(self.queue) >= self.limit:
            return print("queue overflow")

        else:
            if self.isEmpty():
                self.front = self.rear = 0
                self.queue.append(data)
            else:
                self.queue.insert(0, data)
                self.rear += 1

    def dequeue_rear(self):
        if self.isEmpty():
            return print("Queue is empty")

        else:
            self.queue.pop()
            if self.isEmpty():
                self.front = self.rear = None
            else:
                self.rear -= 1

    def findIndex(self, value):
        if self.isEmpty():
            return

        for i in range(len(self.queue)):
            if self.queue[i] == value:
                return i

        return print("no element in queue")


deque = DoubleEndedQueue()

deque.enqueue(10)
deque.enqueue(20)
deque.enqueue_front(5)
deque.enqueue_front(2)
deque.dequeue_rear()

print(deque.queue)

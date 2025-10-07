class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None

    def enqueue(self, data):
        temp = Node(data)

        if self.isEmpty():
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp

    def dequeue(self):
        if self.isEmpty():
            return print("queue is empty")

        temp = self.front
        self.front = temp.next
        temp = None

        if self.front is None:
            self.rear = None

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, data):
        return self.queue.append(data)

    def remove(self):
        if not self.queue:
            return print("is empty")
        else:
            highest_priority_index = self.__getHighestPriorityItem()
            return self.queue.pop(highest_priority_index)

    def peek(self):
        if not self.queue:
            return

        else:
            highest_priority_index = self.__getHighestPriorityItem()
            return self.queue[highest_priority_index][0]

    def update_priorty(self, target_value, new_priorty):
        if not self.queue:
            return

        for i in self.queue:
            if i[0] == target_value:
                i[1] = new_priorty
                return

        return print("item not found")

    def __getHighestPriorityItem(self):
        highest_priority_index = 0

        for i in range(len(self.queue)):
            if self.queue[i][1] > self.queue[highest_priority_index][1]:
                highest_priority_index = i

        return highest_priority_index


pq = PriorityQueue()
pq.insert(["task 1", 10])
pq.insert(["task 2", 5])
pq.insert(["task 3", 30])
pq.update_priorty("task 3", 50)
print(pq.queue)

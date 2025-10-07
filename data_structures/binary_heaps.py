class MinBinaryHeap:
    def __init__(self):
        self.heap = [1, 5, 3, 9, 8, 10, 6]

    def get_parent(self, index):
        if index == 0:
            return None
        return self.heap[(index - 1) // 2]

    def set_parent(self, index, val):
        if index == 0:
            return None
        self.heap[(index - 1) // 2] = val

    def get_left_child(self, index):
        left_child_index = 2 * index + 1
        if left_child_index <= self.size() - 1:
            return self.heap[left_child_index]
        else:
            return None

    def set_left_child(self, index, val):
        left_child_index = 2 * index + 1
        if left_child_index <= self.size() - 1:
            self.heap[left_child_index] = val

    def get_right_child(self, index):
        right_child_index = 2 * index + 2
        if right_child_index == self.size() - 1:
            return self.heap[right_child_index]
        else:
            return None

    def set_right_child(self, index, val):
        right_child_index = 2 * index + 2
        if right_child_index <= self.size() - 1:
            self.heap[right_child_index] = val

    def size(self):
        return len(self.heap)

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.get_parent(index):
                self.heap[index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[index],
                )
                index = parent_index
            else:
                break

    def extract_min(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index] < self.heap[smallest]
        ):
            smallest = left_child_index
        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index] < self.heap[smallest]
        ):
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            self._heapify_down(smallest)

    def get_min(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]


mbh = MinBinaryHeap()
print(mbh.heap)
print("==")
mbh.extract_min()
print(mbh.heap)

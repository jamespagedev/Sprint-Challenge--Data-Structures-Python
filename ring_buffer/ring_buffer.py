class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    # O(1)
    def append(self, item):
        # increment current by 1
        if self.current < len(self.storage) - 1:
            self.storage[self.current] = item
            self.current += 1

        # reset current to first index
        else:
            self.storage[self.current] = item
            self.current = 0

    # O(2n) = O(n)
    def get(self):
        return [x for x in self.storage if x]
        # return [x for x in self.storage[:self.current] if x] + [x for x in self.storage[self.current:] if x]
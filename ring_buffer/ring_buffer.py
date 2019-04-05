class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    # O(1)
    def append(self, item):
        # no overwriting data
        if self.storage[self.current] is None:
            self.storage[self.current] = item

        # reset current to first index
        elif self.current == len(self.storage) - 1:
            self.current = 0
            self.storage[self.current] = item

        # increment current by 1
        else:
            self.current += 1
            self.storage[self.current] = item

    # O(2n) = O(n)
    def get(self):
        return [x for x in self.storage[:self.current] if x] + [x for x in self.storage[self.current:] if x]
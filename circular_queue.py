class CircularQueue:
    def __init__(self, max_length=5):
        self.queue = {}
        self.max_length = max_length
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.max_length == self.front:
            self.dequeue()
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.max_length
        self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return
        elif self.front == self.rear:
            self.queue.pop(self.front)
            self.front = self.rear = -1
        else:
            self.queue.pop(self.front)
            self.front = (self.front + 1) % self.max_length

    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return
        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.max_length):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
        print()


# Example usage:
cq = CircularQueue(max_length=5)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
cq.display()  # Output: 1 2 3 4 5
cq.enqueue(6)
cq.display()  # Output: 2 3 4 5 6
cq.dequeue()
cq.display()  # Output: 3 4 5 6
cq.enqueue(7)
cq.display()  # Output: 3 4 5 6 7

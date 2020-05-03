class Queue:
    data=[]

    def isEmpty(self):
        return self.data == []

    def enqueue(self, data):
        self.data.insert(0,data)

    def dequeue(self):
        return self.data.pop()

    def print_queue(self):
        for data in reversed(self.data):
            print(data)

q = Queue()

q.enqueue('Job 1')
q.enqueue('Job 2')
q.enqueue('Job 3')
q.print_queue()
q.dequeue()
q.dequeue()
q.print_queue()
class Stack:
    data=[]

    def is_empty(self):
        return self.data==[]

    def push(self, node):
        self.data.append(node)

    def pop(self):
        if not self.is_empty():
            value=self.data[-1]
            del self.data[-1]
            return value
        else:
            print("Nothing to pop")

    def print_stack(self):
        for data in reversed(self.data):
            print(data)



fruit = Stack()
fruit.pop()
fruit.push("Apple")
fruit.push("Banana")
fruit.pop()
fruit.push("Canned Yams")
fruit.push("Durian")
fruit.print_stack()
fruit.pop()
fruit.pop()
fruit.print_stack()
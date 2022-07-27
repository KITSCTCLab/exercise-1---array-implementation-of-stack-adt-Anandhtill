import os
class Stack:
    def __init__(self, size):
        self.items = [None]*size
        self.size = size
        self.top = -1

    def is_empty(self):
        if (self.top == -1):
            
            return True
        else:
            return False
        # Write code here

    def is_full(self):
        if (self.top == self.size-1):
           return True
        else:
           return False
        # Write code here

    def push(self, data):
        if not self.is_full():
            self.top += 1
            
            self.items[self.top] = data

            # Write code here

    def pop(self):
        if not self.is_empty():
            data = self.items[self.top]
            
            self.top -= 1
            return data
            # Write code here

    def status(self):
        for i in range(self.top+1):
            
            print(self.items[i])

        # Write code here

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()

import sys
from collections import deque

class Queue:
    def __init__(self, queue):
        self.data = queue()
    
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        return self.data.popleft() if self.data else -1

    def size(self):
        return len(self.data)
    
    def empty(self):
        return 1 if not self.data else 0
        
    def front(self):
        return self.data[0] if self.data else -1
    
    def back(self):
        return self.data[-1] if self.data else -1
        
queue = Queue(deque)
read = sys.stdin.readline
write = sys.stdout.write

n = int(read())
for _ in range(n):
    cmd = read()
    cmd = cmd.strip()
    cmd = cmd.split(' ')

    if cmd[0]=='push':
        queue.push(cmd[1])
    elif cmd[0]=='pop':
        write(str(queue.pop()) + '\n')
    elif cmd[0]=='size':
        write(str(queue.size()) + '\n')
    elif cmd[0]=='empty':
        write(str(queue.empty()) + '\n')
    elif cmd[0]=='front':
        write(str(queue.front()) + '\n')
    elif cmd[0]=='back':
        write(str(queue.back()) + '\n')
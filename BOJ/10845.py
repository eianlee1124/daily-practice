import sys
from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()
    
    def push(self, item):
        self.data.append(item)
    
    def pop(self):
        try:
            return self.data.popleft()
        except:
            return -1

    def size(self):
        return len(self.data)
    
    def empty(self):
        return 1 if not self.data else 0
        
    def front(self):
        try:
            return self.data[0]
        except:
            return -1
    def back(self):
        try:
            return self.data[-1]
        except:
            return -1
        
queue = Queue()
n = int(sys.stdin.readline())
for _ in range(n):
    cmd = sys.stdin.readline()
    cmd = cmd.strip()
    cmd = cmd.split(' ')

    if cmd[0]=='push':
        queue.push(cmd[1])
    elif cmd[0]=='pop':
        sys.stdout.write(str(queue.pop()) + '\n')
    elif cmd[0]=='size':
        sys.stdout.write(str(queue.size()) + '\n')
    elif cmd[0]=='empty':
        sys.stdout.write(str(queue.empty()) + '\n')
    elif cmd[0]=='front':
        sys.stdout.write(str(queue.front()) + '\n')
    elif cmd[0]=='back':
        sys.stdout.write(str(queue.back()) + '\n')

'''

https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

'''

class ArrayQueue:
    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop());
        return self.second[len(self.second)-1];


    def dequeue(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop());
        return self.second.pop();

    def enqueue(self, value):
        self.first.append(value);



queue = ArrayQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.enqueue(values[1])
    elif values[0] == 2:
        queue.dequeue()
    else:
        print(queue.peek())

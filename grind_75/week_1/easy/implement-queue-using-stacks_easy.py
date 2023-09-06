# https://leetcode.com/problems/implement-queue-using-stacks/

from collections import deque

class MyQueue:

    def __init__(self):
        self.temp_stack = deque()
        self.queue = deque()

    def push(self, x: int) -> None:
        current_len = len(self.queue)
        while current_len:
            self.temp_stack.appendleft(self.queue.popleft())
            current_len -= 1

        self.queue.appendleft(x)
        current_len = len(self.temp_stack)
        while current_len:
            self.queue.appendleft(self.temp_stack.popleft())
            current_len -= 1
        

    def pop(self) -> int:
        return self.queue.popleft()

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not bool(len(self.queue))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/

from collections import deque

class Solution:

    def operation(self, operand, value1, value2):
        if operand == '*':
            return value1 * value2
        if operand == "+":
            return value1 + value2
        if operand == '-':
            return value1 - value2
        if operand == '/':
            return int(value1 / value2)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        current_idx = len(tokens)-1

        while current_idx >= 0:
            current_value = tokens[current_idx]
            if current_value in ['+', "-", "/", "*"]:
                stack.appendleft(current_value)
                current_idx -= 1
                continue
            first_element = int(current_value)
            while True:
                try:
                    second_element = stack.popleft()
                except:
                    stack.appendleft(first_element)
                    break
                if second_element in ['+', "-", "/", "*"]:
                    stack.appendleft(second_element)
                    stack.appendleft(first_element)
                    break
                operand = stack.popleft()
                first_element = self.operation(operand, first_element, second_element)
            current_idx -= 1
        
        return stack.popleft()
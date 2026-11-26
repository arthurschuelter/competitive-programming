class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operations = ['+', '-', '*', '/']

        for t in tokens:
            if t in operations:
                b = stack.pop()
                a = stack.pop()

                if t == '+':
                    n = a + b
                elif t == '-':
                    n = a-b
                elif t == '*':
                    n = a * b
                elif t == '/':
                    n = int(a/b)

                stack.append(n)
            else:
                stack.append(int(t))

        return stack.pop()
import pytest

solution = Solution()
@pytest.mark.parametrize("tokens, expected", [
    (["2","1","+","3","*"], 9),
    (["4","13","5","/","+"], 6),
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
])
def test_solution(tokens, expected):
    assert solution.evalRPN(tokens) == expected

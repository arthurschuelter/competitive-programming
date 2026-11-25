class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n_string = [''] * len(s)

        k = 0
        for c in s:
            if ord(c) >= ord('a') and ord(c) <= ord('z') or ord(c) >= ord('0') and ord(c) <= ord('9'):
                n_string[k] = c
                k += 1

        i, j = 0, k-1
        while i < j:
            if n_string[i] != n_string[j]:
                return False
            i += 1
            j -= 1
        
        return True

import pytest

solution = Solution()

@pytest.mark.parametrize("s, expected", [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    ("hello", False)
])

def test_solution(s, expected):
    assert solution.isPalindrome(s) == expected
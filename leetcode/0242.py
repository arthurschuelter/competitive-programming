class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ds = {}
        dt = {}

        for i in range(len(s)):
            if not s[i] in ds:
                ds[s[i]] = 0
            ds[s[i]] += 1

        for i in range(len(t)):
            if not t[i] in dt:
                dt[t[i]] = 0
            dt[t[i]] += 1

        for k, v in ds.items():
            if not k in dt or dt[k] != ds[k]:
                return False

        # if (sorted(s) != sorted(t)):
        #     return False
        return True
        
        

import pytest

solution = Solution()

@pytest.mark.parametrize("s, t, expected", [
    # Test case 1 
    ("anagram", "nagaram", True),
    # Test case 2
    ("rat", "car", False),
    # Test case 3
    ("listen", "silent", True)
])

def test_solution(s, t, expected):
    result = solution.isAnagram(s, t)

    assert result == expected

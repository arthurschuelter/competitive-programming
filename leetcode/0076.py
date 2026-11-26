class Solution:
    def findWindow(self, di, i, t):
        n = len(t)

        j = i
        while j < n:
            ch = t[j]
            if di.get(ch, 0) == 0:
                j += 1
                continue
            # print(t[i:j])

            di[ch] -= 1
            if di[ch] == 0:
                # print(" > pop")
                di.pop(ch) 

            if di == {}:
                # print(f" > achei {i}, {j} : {t[i:j]}")
                return i, j+1, {}

            j += 1

        return i, j, di


    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        ans = (0,0)
        best = len(s)+1

        # Build the dictionary
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1

        n = len(s)
        for i in range(n):
            ch = s[i]
            if d.get(ch, 0) == 0:
                continue
            print(f"({i}) {ch}")
            
            idx_i, idx_j, di = self.findWindow(d.copy(), i, s)

            print(idx_i, idx_j, di)

            if di == {} and idx_j - idx_i < best:
                # print("atualizei")
                best = idx_j - idx_i
                ans = (idx_i, idx_j)

        return s[ans[0]:ans[1]]

import pytest

solution = Solution()

@pytest.mark.parametrize("s, t, expected", [
    ("ADOBECODEBANC", "ABC", "BANC"),
    ("a", "a", "a"),
    ("a", "aa", ""),
    ("ab", "a", "a"),
])

def test_solution(s, t, expected):
    assert solution.minWindow(s, t) == expected


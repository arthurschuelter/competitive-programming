class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        char_set = set(s)

        for c in char_set:
            count_k = 0
            l = 0

            for r in range(len(s)):
                # print(f"[{c}] -> l:{l} | r:{r} | window_size: {r - l + 1}" )
                if s[r] != c:
                    count_k += 1

                while count_k > k:
                    if s[l] != c:
                        count_k -= 1
                    l += 1
                
                res = max(res, r - l + 1)                        


        return res


import pytest

solution = Solution()

@pytest.mark.parametrize("s, k, expected", [
    ("XYYX", 2, 4),
    ("AAABABB", 1, 5),
])

def test_solution(s, k, expected):
    assert solution.characterReplacement(s, k) == expected

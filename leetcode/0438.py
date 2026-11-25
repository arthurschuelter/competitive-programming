class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []
        
        n = len(s)
        ans = []
        word_size = len(p)

        # Build the hash table
        char_count = {}
        original_count = {}
        for ch in p:
            char_count[ch] = char_count.get(ch, 0) + 1
            original_count[ch] = original_count.get(ch, 0) + 1

        r = 0
        for l, ch in enumerate(s):
            # Is this part of the word?
            #   No  => next ch
            #   Yes => go on
            if char_count.get(ch, -1) == -1:
                continue

            if char_count[ch] < original_count[ch]:
                char_count[ch] += 1
            
            if r <= l:
                r = l+1
            
            char_count[ch] -= 1
            while r-l < word_size and r < n:
                if char_count.get(s[r], 0) == 0:
                    break
                
                char_count[s[r]] -= 1
                r += 1
            
            if (r-l == word_size):
                ans.append(l)
            
            char_count[ch] += 1

        return ans
    
    def findAnagrams2(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []
        
        n = len(s)
        ans = []
        word_size = len(p)

        # Build the hash table
        char_count = {}
        for ch in p:
            char_count[ch] = char_count.get(ch, 0) + 1

        window_count = {}
        for ch in s[0:word_size]:
            window_count[ch] = window_count.get(ch, 0) + 1

        for l, ch in enumerate(s):
            r = l + word_size

            if window_count == char_count:
                ans.append(l)
            
            if r == n:
                break
            
            window_count[ch] -= 1
            if window_count[ch] == 0:
                window_count.pop(ch)

            window_count[s[r]] = window_count.get(s[r], 0) + 1

        return ans
    

import pytest

solution = Solution()

@pytest.mark.parametrize("s, p, expected", [
    ("cbaebabacd", "abc", [0,6]),
    ("abab", "ab", [0,1,2]),
    ("abab", "abadasda", []),
])

def test_solution(s, p, expected):
    assert solution.findAnagrams(s, p) == expected
    assert solution.findAnagrams2(s, p) == expected

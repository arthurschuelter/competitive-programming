from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq = [0] * k
        count = Counter(nums)

        i = 0
        for key, v in count.items():
            if i == k:
                break
            
            freq[i] = key
            i += 1

        return freq
        


import pytest

solution = Solution()

@pytest.mark.parametrize("nums, k, expected", [
    # Test case 1 
    ([1,1,1,2,2,3], 2, [1,2]),
    # Test case 2
    ([1], 1, [1]),
    # Test case 3
    ([1,2,1,2,1,2,3,1,3,2], 2, [1, 2]),
])

def test_solution(nums, k, expected):
    result = solution.topKFrequent(nums, k)

    assert sorted(result) == sorted(expected)

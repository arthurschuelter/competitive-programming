class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        freq = {0: 1}

        for n in nums:
            prefix += n
            count += freq.get(prefix - k, 0)
            freq[prefix] = freq.get(prefix, 0) + 1

        return count


import pytest

solution = Solution()

@pytest.mark.parametrize("nums, k, expected", [
    # Test case 1
    ([1, 1, 1], 2, 2),
    # Test case 2
    ([1, 2, 3], 3, 2),
    ([1], 0, 0),
])

def test_solution(nums, k, expected):
    result = solution.subarraySum(nums, k)

    assert result == expected

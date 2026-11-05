from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n-1

        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
    
        return [l+1, r+1]


import pytest

solution = Solution()

@pytest.mark.parametrize("nums, target, expected", [
    # Test case 1 
    ([2,7,11,15], 9, [1,2]),
    # Test case 2
    ([2,3,4], 6, [1,3]),
])

def test_solution(nums, target, expected):
    result = solution.twoSum(nums, target)

    assert result == expected

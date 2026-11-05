from typing import List
class Solution:
    # Time:     O(n)
    # Space:    O(1)
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        return self.binarySearch(nums, l, r)

    def binarySearch(self, nums: List[int], l: int, r: int) -> int:
        if l >= r:
            return nums[l]

        n = len(nums)   
        mid = (l + r) // 2

        # print(f"l: {l} | r: {r} | mid: {mid} | nums[mid]: {nums[mid]}")

        if nums[(mid + 1) % n] < nums[mid]:
            return nums[(mid + 1) % n]
        elif nums[mid] > nums[r]:
            return self.binarySearch(nums, mid+1, r)
        else:
            return self.binarySearch(nums, l, mid)


import pytest

solution = Solution()

@pytest.mark.parametrize("nums, expected", [
    # Test case 1 
    ([3,4,5,1,2], 1),
    # Test case 2
    ([4,5,6,7,0,1,2], 0),
    # Test case 2
    ([11,13,15,17], 11),
])

def test_solution(nums, expected):
    result = solution.findMin(nums)

    assert result == expected

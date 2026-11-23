from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n-1

        max_area = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            max_area = max(area, max_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area

import pytest

solution = Solution()

@pytest.mark.parametrize("height, expected", [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1),
])

def test_solution(height, expected):
    assert solution.maxArea(height) == expected


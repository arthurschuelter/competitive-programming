class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = len(nums)-1

            while j < k:
                soma = nums[i] + nums[j] + nums[k]

                if soma > 0:
                    k -=1
                elif soma < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    
        
        return ans

import pytest

solution = Solution()

@pytest.mark.parametrize("list, expected", [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]]),
])

def test_solution(list, expected):
    assert solution.threeSum(list) == expected

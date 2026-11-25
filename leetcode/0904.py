class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        max_count = -1

        for i, f in enumerate(fruits):
            if (len(fruits)-i < max_count):
                break

            baskets = {}
            count = 0

            j = i
            while j < len(fruits):
                baskets[fruits[j]] = baskets.get(fruits[j], 0) + 1
                j += 1

                if len(baskets.items()) > 2:
                    break
                count += 1

            max_count = max(max_count, count)

        return max_count

    def totalFruit2(self, fruits: list[int]) -> int:
        max_count = 0
        basket = {}
        l = 0

        for r, f in enumerate(fruits):
            basket[f] = basket.get(f, 0) + 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1

                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]

                l += 1

            max_count = max(max_count, r - l + 1)

        return max_count
        
import pytest

solution = Solution()
@pytest.mark.parametrize("fruits, expected", [
    ([1,2,1], 3),
    ([0,1,2,2], 3),
    ([1,2,3,2,2], 4),
    ([1,2,0,1], 2),
])
def test_solution(fruits, expected):
    assert solution.totalFruit(fruits) == expected

@pytest.mark.parametrize("fruits, expected", [
    ([1,2,1], 3),
    ([0,1,2,2], 3),
    ([1,2,3,2,2], 4),
    ([1,2,0,1], 2),
])
def test_solution2(fruits, expected):
    assert solution.totalFruit2(fruits) == expected
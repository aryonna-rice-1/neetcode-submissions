from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r
        while l <= r:
            mid = l + ((r - l) // 2)
            hours = 0
            for pile in piles:
                hours += ceil(pile / mid)

            if hours <= h:
                result = min(result, mid)
                r = mid - 1
            else:
                l = mid + 1
        return result
        
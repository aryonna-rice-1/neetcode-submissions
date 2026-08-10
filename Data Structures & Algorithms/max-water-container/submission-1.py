class Solution:
    def maxArea(self, heights: list[int]) -> int:
        result = -1
        i = 0
        j = len(heights) - 1
        while i < j:
            left = heights[i]
            right = heights[j]
            result = max(result, (min(left, right) * (j - i)))
            if left >= right:
                j -= 1
                while j > i:
                    if heights[j] < right:
                        j -= 1
                    else:
                        break
            else:
                i += 1
                while i < j:
                    if heights[i] < left:
                        i += 1
                    else:
                        break
        return result
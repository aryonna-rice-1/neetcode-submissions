from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for mini_array in matrix:
            max = mini_array[-1]
            if target <= max:
                index = bisect_left(mini_array, target)
                if index >= len(mini_array) or mini_array[index] != target:
                    return False
                else:
                    return True
        return False
        
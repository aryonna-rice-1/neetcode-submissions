class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid_index = start + ((end - start) // 2)
            mid_val = nums[mid_index]

            if target < mid_val:
                end = mid_index - 1
            elif target > mid_val:
                start = mid_index + 1
            else: 
                return mid_index
        return -1
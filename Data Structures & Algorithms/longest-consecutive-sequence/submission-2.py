class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        if len(nums) == 0:
            return 0
        abs_max = 1
        for num in unique_nums:
            if num - 1 not in unique_nums:
                curr_max = 1
                curr_num = num
                keep_searching = True
                while keep_searching:
                    if (curr_num + 1 in unique_nums):
                        curr_max += 1
                        curr_num += 1
                    else:
                        abs_max = max(abs_max, curr_max)
                        keep_searching = False
        return abs_max
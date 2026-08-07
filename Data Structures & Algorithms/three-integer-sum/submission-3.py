class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sorted_nums = sorted(nums)
        result = []
        for i in range(len(nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                triplet_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if triplet_sum > 0:
                    right -= 1
                    continue
                if triplet_sum < 0:
                    left += 1
                    continue
                result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                left += 1
                right -= 1

                while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                    left += 1
        return result
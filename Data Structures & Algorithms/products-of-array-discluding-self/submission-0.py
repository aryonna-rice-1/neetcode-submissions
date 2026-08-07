class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]

        postfix = [nums[-1]] * len(nums) 
        i = len(nums) - 2
        while i > -1:
            postfix[i] = postfix[i + 1] * nums[i]
            i -= 1

        result = [None] * len(nums)
        for i in range(len(nums)):
            prefix_value: int
            postfix_value: int
            if i - 1 == -1:
                prefix_value = 1
            else:
                prefix_value = prefix[i - 1]
            if i + 1 == len(nums):
                postfix_value = 1
            else:
                postfix_value = postfix[i + 1]
            result[i] = prefix_value * postfix_value
        return result
        
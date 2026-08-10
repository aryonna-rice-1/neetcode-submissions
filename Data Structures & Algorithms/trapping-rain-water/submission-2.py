class Solution:
    def trap(self, height: List[int]) -> int:
        left = right = 0
        num_heights = len(height)
        left_max = [0] * num_heights
        right_max = [0] * num_heights

        for i in range(num_heights):
            j = -i - 1
            left_max[i] = left
            right_max[j] = right
            left = max(left, height[i])
            right = max(right, height[j])

        summ = 0
        for i in range(num_heights):
            potential = min(left_max[i], right_max[i])
            summ += max(potential - height[i], 0)
        return summ


        
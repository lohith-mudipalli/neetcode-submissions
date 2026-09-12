class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            current_sum = max(num, current_sum + num)
            maximum = max(maximum, current_sum)

        return maximum
        
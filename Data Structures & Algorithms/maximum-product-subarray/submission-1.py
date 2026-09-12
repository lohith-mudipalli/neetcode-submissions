class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            new_max = max(num, num * current_max, num * current_min)

            new_min = min(num, num * current_max, num * current_min)

            current_max = new_max
            current_min = new_min
            result = max(result, current_max)

        return result



        
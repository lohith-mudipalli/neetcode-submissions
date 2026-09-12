class Solution:
    def canJump(self, nums: List[int]) -> bool:

        fast = 0

        for i in range(len(nums)):

            if i > fast:
                return False
            
            fast = max(fast, i + nums[i])

        return True
        
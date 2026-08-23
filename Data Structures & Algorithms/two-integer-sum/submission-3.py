class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}

        for i,n in enumerate(nums):
            component = target - n

            if component in store:
                return [store[component], i]
            
            store[n] = i
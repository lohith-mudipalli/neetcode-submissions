class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Creates a dictionary to store the key and values
        hash ={}

        for i, num in enumerate(nums):
            component = target - num

            if component in hash:
                return [hash[component], i]
            
            hash[num] = i
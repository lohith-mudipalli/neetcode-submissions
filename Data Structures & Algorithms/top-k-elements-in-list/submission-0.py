class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # creates a dictionary to count the number with repeated times.
        counts = {}
        for i in nums:
            counts[i] = 1 + counts.get(i, 0)

        # creates to store the values and indexs as the repeated
        frequency = [[] for j in range(len(nums) + 1)]

        for num, count in counts.items():
            frequency[count].append(num)
        
        result = []
        for m in range(len(frequency)-1, 0, -1):
            for n in frequency[m]:
                result.append(n)
                
                if len(result) == k:
                    return result

        
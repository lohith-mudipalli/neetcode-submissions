class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []

        for current in intervals:

            if current[1] < newInterval[0]:
                result.append(current)

            elif current[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = current

            else:
                newInterval[0] = min(current[0], newInterval[0])
                newInterval[1] = max(current[1], newInterval[1])

        result.append(newInterval)

        return result
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        frequency = {}
        max_frequency = 0
        maxmium = 0
        left = 0

        for right in range(len(s)):
            frequency[s[right]] = 1 + frequency.get(s[right], 0)
            max_frequency = max(max_frequency, frequency[s[right]])

            while (right - left + 1) - max_frequency > k:
                frequency[s[left]] -= 1
                left += 1
                
            maxmium = max(maxmium, right-left+1)
        
        return maxmium
        
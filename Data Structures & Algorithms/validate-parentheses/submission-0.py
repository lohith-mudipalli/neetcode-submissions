class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for i in range(len(s)):
            if s[i] in pairs:
                
                if stack == []:
                    return False

                if stack[-1] != pairs[s[i]]:
                    return False

                stack.pop()
            
            else:
                stack.append(s[i])

        return stack == []
        
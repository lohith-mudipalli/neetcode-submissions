class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        current_window = {}

        for i in range(len(t)):
            need[t[i]] = 1 + need.get(t[i], 0)

        required = len(need)
        have = 0 

        left = 0

        min_length = float("inf")
        best_left = 0
        best_right = 0 

        for right in range(len(s)):
            current_window[s[right]] = 1 + current_window.get(s[right], 0)

            if s[right] in need and current_window[s[right]] == need[s[right]]:
                have += 1

            while have == required:
                window_length = right - left + 1

                if window_length < min_length:
                    min_length = window_length
                    best_left = left
                    best_right = right

                current_window[s[left]] -= 1

                if s[left] in need and current_window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[best_left: best_right + 1]


        
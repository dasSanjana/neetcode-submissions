class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        state = set()
        for right in range(len(s)):
            while s[right] in state:
                state.remove(s[left])
                left += 1
            state.add(s[right])
            ans = max(ans, right - left +1)
        return ans



        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = 0
        frequency = {}
        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right],0) + 1
            while (right - left + 1) - max(frequency.values()) > k:
                frequency[s[left]] -= 1
                left += 1
            max_len = max(max_len,right - left + 1)
        return max_len
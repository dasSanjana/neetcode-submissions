class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char,0)+1
        
        window = {}
        have = 0
        need = len(count_t)

        best_len = float('inf')
        best_start = -1
        best_end = -1

        left = 0
        for right in range(len(s)):
            char_map =  s[right]
            window[char_map] = window.get(char_map,0) + 1

            if char_map in count_t and window[char_map] == count_t[char_map]:
                have += 1
            while have == need:
                current_size = right - left + 1
                if current_size < best_len:
                    best_len = current_size
                    best_start = left
                    best_end = right
            
                left_char = s[left]
                window[left_char] -= 1

                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                left += 1
        if best_len!= float('inf'):
                return s[best_start : best_end + 1]
        return ""


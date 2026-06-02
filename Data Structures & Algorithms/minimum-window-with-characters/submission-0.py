class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_freq = Counter(t)
        window_freq = Counter()
        matched_chars = 0
        left = 0 
        min_start, min_length = -1, float('inf')

        for right, char in enumerate(s):
            window_freq[char] += 1
            
            if char in target_freq and window_freq[char] <= target_freq[char]:
                matched_chars += 1
            
            while matched_chars == len(t):
                window_size = right - left + 1
                if window_size < min_length:
                    min_length = window_size 
                    min_start = left
                
                # contracting the window size down 
                left_char = s[left]
                if left_char in target_freq and window_freq[left_char] <= target_freq[left_char]:
                    matched_chars -= 1
                window_freq[left_char] -= 1
                left += 1

        return "" if min_start == -1 else s[min_start : min_start + min_length]
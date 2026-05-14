class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        result = 0
        n = len(s)

        for c in char_set:
            l = count = 0
            for r in range(n):
                if s[r] == c:
                    count += 1
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                result = max(result, r - l + 1)
                
        return result 
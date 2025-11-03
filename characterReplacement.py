
# 424. Longest Repeating Character Replacement
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        count = {}
        res = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "ABAB"
    k = 2
    print("Output is : ", sol.characterReplacement(s,k))

    s2 = "AABABBA"
    k2 = 1
    print("Output is : ", sol.characterReplacement(s2,k2))

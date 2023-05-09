class Solution:
    def diStringMatch(self, S: str) -> list[int]:
        low, high = 0, len(S) 
        for c in S:
            if c == 'I':
                yield low
                low += 1
            else:
                yield high
                high -= 1
        yield low

s = "IDID"
ss = Solution()
print(list(ss.diStringMatch(s)))
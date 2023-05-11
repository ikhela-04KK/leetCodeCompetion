class Solution(object):
    def prefixCount(self, words, pref):

        for word in words:
            low = word.startswith(pref) 
            yield low
        return sum([low])
  

sol = Solution()
nword = sol.prefixCount(["leetcode","win","loops","success"], pref = "code")
print(list(nword))
print()
from memory_profiler import profile
class Solution(object):
    @profile
    def prefixCount(self, words, pref):
        # n = len(pref)
        # nword = 0
        # for word in words:
        #     if pref in word[:n]:
        #         nword += 1
        return [word.startswith(pref) for word in words] # or pref in word[:len(pref)]


sol = Solution()
nword = sol.prefixCount(["leetcode","win","loops","success"], pref = "code")
print(nword)
print()

nword = sol.prefixCount(["pay","attention","practice","attend"], pref = "at")
print(nword)
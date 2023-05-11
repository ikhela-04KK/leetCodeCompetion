class Solution:
    def con_arr(self,arr):
        arr = arr+arr
        return arr

p1,p2=[1,2,1],[1,3,2,1]
n = Solution()

print(n.con_arr(p1))
print(n.con_arr(p2))

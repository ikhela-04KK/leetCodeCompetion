
class Solution: 
    def diString(self, s):
        n= len(s)
        perm = [0]*(n+1) # creation de len(s) 0
        start,end = 0,n # definis la phase et la fin 

        for i in range(n):
            if s[i] == "I":
                perm[i] = start
                start +=1
            else: 
                perm[i] = end
                end -=1
        perm[n] =start
        return perm

         

        # for i in range(lengP):
        #     arret =False
        #     for j in range(lengS-i):
        #         if s[j] == 'D' and perm[j] < perm[j + 1]:
        #             perm[j],perm[j+1] = perm[j+1],perm[j]
        #             arret =True
        #     if arret == False:
        #         return perm

        



print("-------[0,4,1,3,2]----------")
s= "IDID"
ss = Solution()
print(ss.diString(s))
print("--------[0,1,2,3]------------")
s= "III"
ss = Solution()
print(ss.diString(s))
print("--------[3,2,0,1]-------------")
s= "DDI"
ss = Solution()
print(ss.diString(s))
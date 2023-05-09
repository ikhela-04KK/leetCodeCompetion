# leetCode 561
class Solution:
    def arrayPart(self,nums):
        # sourcery skip: for-append-to-extend, for-index-underscore
        # nums = sorted(nums)
        pair_list = []
        nums = sorted(set(nums))
        
        #creation de la liste de nombre pair
        for i in range(len(nums)-2):
          for j in range(i,len(nums)):
                pair_list.append([nums[i],nums[j]])


        print()
        print(pair_list)
        #determiner la grande addition des nombres issu de l'addition des nombres pairs

        maxi = min(pair_list[0])
        for i in range(0,len(pair_list)-1,2):
            min_max = min(pair_list[i])+min(pair_list[i+1])
        if maxi < min_max:
           maxi = min_max
        print(maxi)


num1s =Solution() 
num1s.arrayPart([1,4,3,2])

num2s = Solution()
num2s.arrayPart([6,2,6,5,1,2])


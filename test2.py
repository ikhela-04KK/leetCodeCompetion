
def arrayPart(nums):  # sourcery skip: for-append-to-extend
    pair_list = []

    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            pair_list.append([nums[i],nums[j]])
    print(pair_list)
    maxi = float('-inf')
    for i in range(0,len(pair_list)-1,2):
        pair_sum = min(pair_list[i])+min(pair_list[i+1])
        if pair_sum > maxi:
            maxi = pair_sum

    print(maxi)


nums = [1,4,3,2]
arrayPart(nums)

num1s = [6,2,6,5,1,2]
arrayPart(num1s)

nums = [[1,2] , [2,5], [1,2], [5,2]]

unikList = list(dict.fromkeys(map(tuple,nums)))
unikList = [list(x) for x in unikList]
print(unikList)




# le but du problème était de faire en sorte de trouver la difference la plus petite entre le maximum et le minimum
class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        x=max(nums)
        y=min(nums)
        return max(0,(x-k)-(y+k))




class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        num=float('inf')
        for i in nums:
            a=abs(num)
            if abs(i) < a:
                num=i
            elif i == a:
                if i>num:
                    num=i
        return num
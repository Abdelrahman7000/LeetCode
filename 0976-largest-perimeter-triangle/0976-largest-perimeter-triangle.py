class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums=sorted(nums)
        def is_valid(a,b,c):
            if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
                return False
            else:
                return True     
        
        i=len(nums)-1
        res=-1
        while i>=2:
            a=nums[i]
            b=nums[i-1]
            c=nums[i-2]
            if not is_valid(a,b,c):
                i=i-1
                continue
            else:
                res=a+b+c
                break
        return 0 if res==-1 else res
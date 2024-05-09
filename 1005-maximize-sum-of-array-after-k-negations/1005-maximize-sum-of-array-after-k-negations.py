class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        nums=sorted(nums)
        
        for idx in range(len(nums)):
            if nums[idx]<0 and k>0:
                nums[idx]*=-1
                k-=1
            elif nums[idx]>=0 or k==0:
                break
        
        if k%2 !=0:
            nums=sorted(nums)
            nums[0]*=-1
        return sum(nums)
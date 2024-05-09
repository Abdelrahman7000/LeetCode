class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        nums=sorted(nums)
        def has_neg(lst):
            neg=0
            for item in lst:
                if item < 0:
                    neg+=1
            return neg
        
        negatives=has_neg(nums)
        if negatives>0:
            if k>=negatives:
                for i in range(negatives):
                    nums[i]*=-1
                    k-=1
                nums=sorted(nums)
                if k%2==0 or k==0:
                    return sum(nums)
                else:
                    nums[0]*=-1
                    return sum(nums)
            if k<negatives:
                for i in range(k):
                    nums[i]*=-1

                return sum(nums)
        else:
            if k%2==0:
                return sum(nums)
            else:
                nums[0]*=-1
                return sum(nums)
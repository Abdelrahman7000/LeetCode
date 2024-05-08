class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # def sorting(arr):
        #     for i in range(len(arr)-1):
        #         j=i+1
        #         while arr[j]<arr[i] and i>=0 :
        #             arr[i],arr[j]=arr[j],arr[i]
        #             j-=1
        #             i-=1
        #     return arr

        
        arr = sorted(arr)
        pairs=[]
        min_diff=0
        for i in range(len(arr)-1):
            diff=abs(arr[i+1]-arr[i])
            if not pairs:
                pairs.append([arr[i],arr[i+1]])
                min_diff=diff
                continue
            if diff==min_diff:
                pairs.append([arr[i],arr[i+1]])
                continue
            if diff > min_diff:
                continue
            pairs.clear()
            min_diff=diff
            pairs.append([arr[i],arr[i+1]])
        return pairs
                
        
        
       
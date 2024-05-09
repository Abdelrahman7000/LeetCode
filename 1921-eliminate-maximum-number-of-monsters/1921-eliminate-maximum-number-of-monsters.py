class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n=len(dist)
        time=[ dist[i]/speed[i] for i in range(n)]
        time=sorted(time)
        for idx,val in enumerate(time):
            if val<=idx:
                return idx
        return n
     
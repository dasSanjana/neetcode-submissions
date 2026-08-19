class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        final = sorted(count.keys(),key = lambda x: count[x],reverse= True)
        return final[:k]
        
                
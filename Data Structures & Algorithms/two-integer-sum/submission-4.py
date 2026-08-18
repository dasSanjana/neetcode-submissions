class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final = []
        for n in range(len(nums)):
            for i in range(n+1,len(nums)):
                sub = target - nums[n]
                if sub == nums[i]:
                    final.append(n)
                    final.append(i)
                    break
            
        return final
                    
        
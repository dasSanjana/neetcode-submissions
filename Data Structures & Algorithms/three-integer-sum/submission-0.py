class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()
        for i , v in enumerate(nums):
            if i > 0 and nums[i-1] == v:
                continue

            j = i+1
            k = len(nums)-1
            while j < k:
                three_sum =  v + nums[j] + nums[k] 
                if three_sum < 0:
                    j +=1
                elif three_sum > 0:
                    k-=1
                else:
                    final.append([nums[i],nums[j],nums[k]])
                    j +=1
                    k -=1
                    while nums[j] == nums[j-1] and j < k :
                        j += 1           
        return final
            


class Solution:
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		end,result,tp_sum=0,nums[0],0
		while end<len(nums):
			tp_sum+=nums[end]
			result=max(result,tp_sum)
			tp_sum=max(tp_sum,0)
			end=end+1
		return result


tp=Solution()
print(tp.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(tp.maxSubArray([0]))
print(tp.maxSubArray([-3,-2,0,-1]))
print(tp.maxSubArray([-2,-1]))
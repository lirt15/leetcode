class Solution:
	def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if len(nums)<2:return True
		start,end=0,0
		while end < len(nums)-1:
			start,end=end+1,max([nums[i]+i for i in range(start,end+1)])
			if end < start:
				return False
		return True
tp=Solution()
print(tp.canJump([2,0,0]))
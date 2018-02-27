class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		arr=[i for i in range(1000)]
		for n in nums:
			if n>0:
				arr[n]=-1
		for it in arr:
			if it > 0:
				return it
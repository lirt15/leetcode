class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		def sub_permute(ns):
			if not ns: return [ns]
			result=[]
			for i in range(len(ns)):
				for j in sub_permute(ns[:i]+ns[i+1:]):
					result.append([ns[i]]+j)
			return result
		return sub_permute(nums)

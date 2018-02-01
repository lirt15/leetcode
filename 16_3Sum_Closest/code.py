class Solution(object):
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		nums=sorted(nums)
		result=nums[0]+nums[1]+nums[2]
		for i in range(len(nums)-2):
			l,r=i+1,len(nums)-1
			while r>l:
				s=nums[i]+nums[l]+nums[r]
				if abs(s-target)<abs(result-target):	result=s
				if s>target: r-=1
				elif s<target: l+=1
				else: return target
		return result
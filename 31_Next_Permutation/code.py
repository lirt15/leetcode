class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		len_nums,flag=len(nums),True
		if len_nums==0 or len_nums==1:return
		for break_point in range(len_nums-2,-1,-1):
			if nums[break_point]<nums[break_point+1]:
				flag=False
				break
		if flag: 
			nums[:] = nums[::-1]
			return
		for change_point in range(len_nums-1,-1,-1):
			if nums[change_point]>nums[break_point]:
				break

		tp_slice=nums[break_point:]
		tp_slice.pop(change_point-break_point)
		nums[break_point:]=[nums[change_point]]+sorted(tp_slice)
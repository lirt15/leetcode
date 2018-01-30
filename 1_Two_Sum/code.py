class Solution(object):
	def twoSum(self, nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]
	"""
	num_dict={}
	for num_index in range(len(nums)):
		if target-nums[num_index] in num_dict:
			return [num_dict[target-nums[num_index]],num_index]
		else:
			num_dict[nums[num_index]]=num_index

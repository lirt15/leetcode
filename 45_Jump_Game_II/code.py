class Solution(object):
	def jump(self, nums):
		if len(nums)==1:return 0
		step,start,end=0,0,0
		while True:
			start,end,step=end+1,max([start+i+nums[start+i] for i in range(end-start+1)]),step+1
			if end>=len(nums)-1:
				return step
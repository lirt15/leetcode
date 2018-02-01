class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		if len(nums)<3:return []
		num_dict={}
		result=set([])
		for num in nums:
			if num in num_dict: num_dict[num]+=1
			else: num_dict[num]=1
		set_tp=set(nums)
		for i in set_tp:
			for j in set_tp:
				if i==j and num_dict[i]<2:
					continue
				tp=-i-j
				if tp in num_dict and num_dict[tp]>(int(i==tp)+int(tp==j)):
					result.add(tuple(sorted((i,j,tp))))
		result=[it for it in map(lambda a:list(a),result)]
		return result

tp=Solution()
print(tp.threeSum([-1, 0, 1, 2, -1, -4]))
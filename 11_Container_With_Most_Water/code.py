class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		head,tail,result=0,len(height)-1,0
		while tail>head:
			if height[tail]>height[head]:
				result=max(result,(tail-head)*height[head])
				head+=1
			else:
				result=max(result,(tail-head)*height[tail])
				tail-=1
		return result
import time
class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		if len(height)<3:return 0
		result,left,right=0,height[0],max(height[2:])
		index=height[2:].index(right)+2
		for i in range(1,len(height)-1):
			result+=max(min(left,right)-height[i],0)
			if i >= index: 
				right=max(height[i+1:])
				index=height[i:].index(right)+i
			left=max(left,height[i])
		return result

t=time.time()
tp=Solution()
print(tp.trap([4,2,3]))
print(time.time()-t)

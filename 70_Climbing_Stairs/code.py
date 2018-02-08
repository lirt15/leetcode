class Solution(object):
	def climbStairs(self, num):
		tp=[1,1]
		for _ in range(2,num+1):
			tp.append(tp[-1]+tp[-2])
		return tp[-1]
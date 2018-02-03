class Solution(object):
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		if x==0:return 0
		left,right=1,x
		while True:
			tp=int((left+right)/2)
			if tp**2>x:
				right = tp
			elif tp**2<x and left!=right-1:
				left =tp
			else:
				return tp
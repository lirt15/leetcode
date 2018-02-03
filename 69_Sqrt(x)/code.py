class Solution(object):
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		if x==0:return 0
		y=1
		while y**2<x:
			y=2*y
		y2=int(y/2)
		if y**2==x:return y
		left,right=y2,y
		while True:
			tp=int((left+right)/2)
			if tp**2>x:
				right = tp
			elif tp**2<x and left!=right-1:
				left =tp
			else:
				return tp
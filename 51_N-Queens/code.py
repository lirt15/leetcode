class Solution:
	def solveNQueens(self, n):
		"""
		:type n: int
		:rtype: List[List[str]]
		"""
		queens=[(i,0) for i in range(n)]
		result=[]
		
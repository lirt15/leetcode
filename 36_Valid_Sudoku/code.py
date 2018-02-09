class Solution(object):
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""
		def judge_line(st):
			for line in st:
				tp=[]
				for cha in line:
					if cha=='.': continue
					elif cha in tp:		return False
					else: tp.append(cha)
		if judge_line(board)==False:
			return False
		if judge_line([[board[i][j] for i in range(9)] for j in range(9)])==False:
			return False
		if judge_line([board[i-1][j-1:j+2]+board[i][j-1:j+2]+board[i+1][j-1:j+2] for j in [1,4,7] for i in [1,4,7] ])==False:
			return False
		return True
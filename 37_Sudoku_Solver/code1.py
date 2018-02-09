class Solution(object):
	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		"""
		from functools import reduce
		all_val=[[{} for _ in range(9)] for _ in range(9)]
		def judge_set(bd,i,j):
			ro,co=int(i/3)*3+1,int(j/3)*3+1
			tp1=set(board[i])|set([board[t][j] for t in range(9)])
			tp2=set(bd[ro-1][co-1:co+2]+bd[ro][co-1:co+2]+bd[ro+1][co-1:co+2])
			tp=tp1|tp2
			return tp-{'.'}

		i,j=0,0
		for i in range(9):
			for j in range(9):
				if board[i][j]=='.':
					tp=judge_set(board,i,j)
					all_val[i][j]=set(['1','2','3','4','5','6','7','8','9'])-tp		
		while True:
			if i==9:break
			if len(all_val[i][j])==1:
				board[i][j]=list(all_val[i][j])[0]

			j=(j+1)%9
			i+=int(j==0)
			"""
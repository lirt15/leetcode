class Solution(object):
	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		def judge_set(bd,i,j):
			ro,co=int(i/3)*3+1,int(j/3)*3+1
			tp1=set(board[i])|set([board[t][j] for t in range(9)])
			tp2=set(bd[ro-1][co-1:co+2]+bd[ro][co-1:co+2]+bd[ro+1][co-1:co+2])
			tp=         tp1|tp2
			return tp-{'.'}
		i,j=0,0
		while True:
			print(i,j)
			if i==9:break
			if board[i][j]=='.':
				tp=judge_set(board,i,j)
				if len(tp)==8:
					board[i][j]=list(set(['1','2','3','4','5','6','7','8','9'])-tp)[0]
					print('!!!!!',i,j,board[i][j],tp)
					i,j=0,0
					print(i,j)
					continue
				else:
					j=(j+1)%9
					if j==0:
						i+=1
			else:
				j=(j+1)%9
				if j==0:
					i+=1
		
b=[[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
print('--------------------')
for it in b:
    print(it)
print('--------------------')
tp=Solution()
tp.solveSudoku(b)
for it in b:
    print(it)
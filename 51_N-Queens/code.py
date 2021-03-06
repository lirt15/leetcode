class Solution:
	def solveNQueens(self, n):
		import itertools
		result=[]
		for pl in itertools.permutations(range(n),n):
			r_c,c_r,flag={},{},True
			for r,c in zip(range(n),pl):
				if r-c in r_c or r+c in c_r:
					flag=False
					break
				else:
					r_c[r-c],c_r[r+c]=1,1
			if flag:
				result.append(['.'*c+'Q'+'.'*(n-c-1) for r,c in zip(range(n),pl)])
		return result			
tp=Solution()
print(tp.solveNQueens(9))
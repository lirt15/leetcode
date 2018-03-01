class Solution(object):
	def rotate(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: void Do not return anything, modify matrix in-place instead.
		"""
		len_m,center=len(matrix),(len(matrix)-1)/2
		for r in range(int(len_m/2)):
			for c in range(r,len_m-r-1):
				x,y=[r-center,c-center,center-r,center-c],[c-center,center-r,center-c,r-center]
				matrix[int(x[0]+center)][int(y[0]+center)],matrix[int(x[1]+center)][int(y[1]+center)],matrix[int(x[2]+center)][int(y[2]+center)],matrix[int(x[3]+center)][int(y[3]+center)]=\
				matrix[int(x[3]+center)][int(y[3]+center)],matrix[int(x[0]+center)][int(y[0]+center)],matrix[int(x[1]+center)][int(y[1]+center)],matrix[int(x[2]+center)][int(y[2]+center)]

tp=Solution()
a=[[1,2,3],[4,5,6],[7,8,9]]
tp.rotate(a)
print(a)
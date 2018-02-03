class Solution(object):
	def generateParenthesis(self, n):
		from itertools import combinations
		import re
		"""
		:type n: int
		:rtype: List[str]
		"""
		result,nums=[],[2**i for i in range(2*n)]
		tp_list=list(combinations(nums, n))
		for item in tp_list:
			stack,flag,tp_string=[],True,bin(sum(item)+2**(2*n))[3:]
			for cha in tp_string:
				if cha=='1':stack.append(cha)
				else:
					if len(stack)==0:
						flag=False
						break
					else:
						stack=stack[:-1]
			if flag:
				result.append(re.sub('0',')',re.sub('1','(',tp_string)))
		return result
tp=Solution()
print(tp.generateParenthesis(2))
class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		stack,dic=[],{'(':')','[':']','{':'}'}
		for cha in s:
			if cha in dic.keys():
				stack.append(cha)
			elif cha in dic.values():
				if len(stack)>0 and dic[stack[-1]]==cha:
					stack=stack[:-1]
				else:
					return False
		if len(stack)>0:
			return False
		return True
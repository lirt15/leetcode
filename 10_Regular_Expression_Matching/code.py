class Solution(object):
	def isMatch(self, s, p):
		# I give up this one
		"""
		:type s: str
		:type p: str
		:rtype: bool
		"""
		'''
		s_dict={}
		for cha_num in range(len(s)):
			if s[cha_num] in s_dict:
				s_dict[s[cha_num]].append(cha_num)
			else:
				s_dict[s[cha_num]]=[cha_num]

		p_len,s_len=len(p),len(s)

		p_list=[i for i in range(p_len)]
		while True:
			pointer_s=0
			for i in range(p_len):
				if p[i] =='*' or p[i]=='.':
					continue

				if p[i]!=s[pointer_s]:
					if p_list[-1]==s_len-1:
		'''


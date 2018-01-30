class Solution(object):
	def lengthOfLongestSubstring(self,s):
		start,cha_dict,result=0,{},0
		for it in range(len(s)):
			sit=s[it]
			if sit in cha_dict and cha_dict[sit] >=start:
				start=cha_dict[sit]+1
			else:
				result=max(it - start +1,result)
			cha_dict[sit]=it
		return result
class Solution:
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""
		dic={}
		for ch in strs:
			if tuple(sorted(list(ch))) in dic:
				dic[tuple(sorted(list(ch)))].append(ch)
			else:
				dic[tuple(sorted(list(ch)))]=[ch]
		return list(dic.values())

tp=	Solution()
print(tp.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
class Solution(object):
	def permuteUnique(self, nums):
		def sub_permute(ns):
			if not ns: return [ns]
			result,ns=[],sorted(ns)
			for i in range(len(ns)):
				if ns[i]==ns[i-1] and i>0:continue
				for j in sub_permute(ns[:i]+ns[i+1:]):
					result.append([ns[i]]+j)
			return result
		tp=[list(tt) for tt in set([tuple(t) for t in sub_permute(nums)])]
		return tp
tp=Solution()
print(tp.permuteUnique([3,3,1,2,3,2,3,1]))
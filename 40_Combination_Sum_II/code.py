class Solution(object):
	def combinationSum2(self, candidates, target):
		"""
		:type candidates: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		def sub_array(arr,tar,loc):
			sub_result=[]
			for item in range(loc,len(arr)):
				if arr[item]<tar:
					tp=sub_array(arr,tar-arr[item],item+1)
					for tmp in tp:
						sub_result.append([arr[item]]+tmp)
				elif arr[item]==tar:
					sub_result.append([arr[item]])
				else:
					break
			return sub_result
		tp = [it for it in map(lambda a:tuple(a),sub_array(sorted(candidates),target,0))]
		tp=set(tp)
		tp = [it for it in map(lambda a:list(a),tp)]
		return tp 

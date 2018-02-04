def longestValidParentheses(s):
		queue,index=[0 for _ in range(len(s))],[]
		for i in range(len(s)):
			if s[i]=='(':
				index.append(i)
			else:
				if index:
					queue[index.pop()],queue[i]=1,1
		result,cnt=0,0
		for i in queue:
			if i==0:
				cnt,result=0,max(cnt,result)
			else:
				cnt+=1
		return max(result,cnt)
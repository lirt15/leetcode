class Solution(object):
    def longestPalindrome(self, s):
        max_str=""
        max_len=int(len(s)>0)
        if len(s)>0:   max_str=s[0]
        for i in range(1,len(s)):
            if i-max_len-1>=0 and s[i-max_len-1:i+1]==s[i-max_len-1:i+1][::-1]:
                max_str=s[i-max_len-1:i+1]
                max_len+=2
                continue
            if s[i-max_len:i+1]==s[i-max_len:i+1][::-1]:
                max_str=s[i-max_len:i+1]
                max_len+=1
        return max_str
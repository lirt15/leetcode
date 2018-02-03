class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gen(p, left, right, res = []):
            if left:gen(p+'(', left-1, right, res)
            if right > left : gen(p+')', left, right-1, res)
            if not right:res.append(p)
            
            return res
        return gen('', n, n, [])
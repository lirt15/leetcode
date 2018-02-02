class Solution(object):
    def letterCombinations(self, digits):
        if '' == digits: return []
        digit_dict={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        result=reduce(lambda acc, digit: [x + y for x in acc for y in digit_dict[digit]], digits, [''])
        return result
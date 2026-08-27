class Solution(object):
    def reverseWords(self, s):
        i=len(s)-1
        ans=""
        while i>=0:
            while i>=0 and s[i]==" ":
                i-=1
            if i<0:
                break
            end=i
            while i>=0 and s[i]!=" ":
                i-=1
            word=s[i+1:end+1]
            if ans!="":
                ans+=" "
            ans+=word
        return ans

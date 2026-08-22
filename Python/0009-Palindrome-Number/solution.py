class Solution(object):
    def isPalindrome(self,x):
        rev=0
        copy=x

        if x<0:
            return False

        while x>0:
            d = x%10
            rev = (rev*10)+d
            x//=10

        if rev == copy:
            return True
        else:
            return False

x= int(input())
s = Solution()
print(s.isPalindrome(x))
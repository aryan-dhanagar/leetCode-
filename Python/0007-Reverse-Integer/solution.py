class Solution(object):
    def reverse(self,x):
        rev = 0
        if x < 0:
            neg = 1
            x = abs(x)  
        else:
            neg = 0
        while x>0:
            ld= x%10
            rev = (rev*10)+ld
            x //=10
        if rev <= (2**31) - 1 and rev> -2**31:
            if neg == 1:
                rev = -rev
                return rev
            else:
                return rev
        else:
            return 0
x = int(input())
s = Solution()
print(s.reverse(x))


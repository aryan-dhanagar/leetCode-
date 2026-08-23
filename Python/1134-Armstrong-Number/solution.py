class Solution(object):
    def isArmstrong(self,n):
        copy = n
        total = 0
        nod = len(str(n))
        while n>0:
            d = n%10
            total = total + (d**nod)
            n//=10
        if total == copy:
            return True
        else:
            return False

n = int(input())
s = Solution()
print(s.isArmstrong(n))
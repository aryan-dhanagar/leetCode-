class Solution(object):
    def isArmstrong(self,n):
        copy = n
        copy2 =n
        total = 0
        count=0
        while copy>0:
            copy//=10
            count+=1 

        while n>0:
            d = n%10
            total = total + (d**count)
            n//=10
        if total == copy2:
            return True
        else:
            return False

n = int(input())
s = Solution()
print(s.isArmstrong(n))
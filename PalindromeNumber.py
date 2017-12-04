"""

LeetCode #9 
Determine whether an integer is a palindrome. Do this without extra space.

Solution:
O(log10) time complexity
compare the first half of the integer with the second half

Note: convert int to string, and then reverse the string to get the reverse integer will work, but this require additional O(n) memory
e.g. 
X=str(x)
X=int(X[::-1])
return x==X

"""



class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x>0 and x%10==0):
            rtype=bool(0)
        else:
            new=x%10
            while new<x:
                x=x/10
                new=new*10+x%10                
            rtype= (new==x) or (new==x*10+new%10)                                 
        return rtype

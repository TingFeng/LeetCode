
"""
LeetCode #191: Number of 1 bits

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        # solution 1: count 1 in integer 
        
        count=0
        x=int(bin(n)[2:])
        while x>0:
            if x%10==1:
                count=count+1
            x=x/10
        
        # solution 2: count '1' from string
        
        count=0
        for x in list(bin(n)[2:]):
            if x=='1':
                count=count+1
        
        """
        
        # Solution 3: bit manipulation n & n-1 will make the low digits 0 
        
        count=0
        while n!=0:
            count=count+1
            n=n & n-1                
              
        return count

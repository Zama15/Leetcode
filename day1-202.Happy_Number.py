# 202. Happy Number
# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 1 + 81 = 82
# 8^2 + 2^2 = 64 + 4 = 68
# 6^2 + 8^2 = 36 + 64 = 100
# 1^2 + 0^2 + 0^2 = 1 + 0 + 0 = 1
# Example 2:

# Input: n = 2
# Output: false
 

# Constraints:

# 1 <= n <= 2^31 - 1

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n == 1 or int(list(str(n)).pop()) == 1:
            return True

        number = list(str(n))

        addition = 0

        for x in number:
            addition += int(x) ** 2

        if len(str(addition)) == 1:
            return True if addition == 1 else False
        else:
            return self.isHappy(addition)
        

# Failure

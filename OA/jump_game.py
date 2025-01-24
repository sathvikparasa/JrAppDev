# Sathvik Parasa
# 922076112
# Jr. Application Developer - STDT 4 (HS # 9534690)
# Jump Game Leetcode OA

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
            Explanation: I thought about iterating through the array backwards,
            checking if I could reach the last element from each new element backwards.
            This method ensures O(n) time complexity as well.
        """
        # Last will be used to store the index of the element that we need to reach
        last = len(nums) - 1
        # Curr will be used to store the index of the element that we are checking for jump charges
        curr = last - 1
        # Use a while loop to check all elements of nums
        while(curr >= 0):

            # If you can reach at least the last element
            if(nums[curr] + curr >= last):
                # Go make that element the last element
                last = curr
            # Iterate curr backwards
            curr -= 1
        
        # If the index of the element that we need to reach is 0, then we know that the jump game is possible
        return True if (last == 0) else False




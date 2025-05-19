# 740. Delete and Earn
# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.


# Example 1:

# Input: nums = [3,4,2]
# Output: 6
# Explanation: You can perform the following operations:
# - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
# - Delete 2 to earn 2 points. nums = [].
# You earn a total of 6 points.
# Example 2:

# Input: nums = [2,2,3,3,3,4]
# Output: 9
# Explanation: You can perform the following operations:
# - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
# - Delete a 3 again to earn 3 points. nums = [3].
# - Delete a 3 once more to earn 3 points. nums = [].
# You earn a total of 9 points.


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # regresar el maximo numero de puntos que puedo conseguir
        # borro los numeros de la lista que sean igual a el numero de puntos +1 o -1
        # sumo todos los numeros que no fueron borrados de la lista con los puntos que ya tenia

        max_list = nums
        maximo = max_list.index(max(max_list))
        max_points_init = max_list.pop(maximo)
        max_points = 0

        if len(max_list) != 0:
            for i in range(len(max_list)):
                if max_list[i] != max_points_init + 1 and max_list[i] != max_points_init - 1:
                    max_points += max_list[i]

        com_list = nums
        com_points_init = 0
        com_points = 0
        if len(com_list) != 0:
            commoner = com_list.index(Counter(com_list).most_common(1)[0][0])
            com_points_init = com_list.pop(commoner)
            com_points = 0

            for i in range(len(com_list)):
                if com_list[i] != com_points_init + 1 and com_list[i] != com_points_init - 1:
                    com_points += com_list[i]

        max_total = max_points_init + max_points
        com_total = com_points_init + com_points
        
        return max_total if max_total > com_total else com_total
        

# Failure

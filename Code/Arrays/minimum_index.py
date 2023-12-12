class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # Step1 is to check the string is present in both the lists
        # Step2 is note the string and their index sum values
        # Step3 is to take the minimum values of the sum and return the corresponding strings
        sum_index = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if (i + j) not in sum_index:
                        sum_index[i + j] = [list1[i]]
                    else:
                        sum_index[i + j].append(list1[i])

        return sum_index[min(sum_index.keys())]


newObj = Solution()
print(newObj.findRestaurant(["happy", "sad", "good"], ["sad", "happy", "good"]))

# Output: ["happy","sad"]

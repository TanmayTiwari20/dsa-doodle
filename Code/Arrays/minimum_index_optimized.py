class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # Step1 is to create a dict containing list values and their indices
        # Step2 is to create a inf number which we can update everytime we see a smaller number
        # Step3 is to iterate over list2 and check if the current value is in the dict:
        # Step3.1 is to create a sum of the 2 indexes
        # Step3.1.a is to check weather sum is smaller than current min sum, update the min sum to current sum,add common item to return list
        # Step2 is note the string and their index sum values
        # Step3 is to take the minimum values of the sum and return the corresponding strings
        hashmap = {}

        for i in range(len(list1)):
            hashmap[list1[i]] = i

        result = []
        min_sum = float("inf")

        for j in range(len(list2)):
            if list2[j] in hashmap:
                sum_index = hashmap[list2[j]] + j
                if sum_index < min_sum:
                    min_sum = sum_index
                    result = []
                    result.append(list2[j])
                elif sum_index == min_sum:
                    result.append(list2[j])
        return result


newObj = Solution()
print(newObj.findRestaurant(["happy", "sad", "good"], ["sad", "happy", "good"]))

# Output: ["happy","sad"]

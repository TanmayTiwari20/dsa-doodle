nums = [0, 1, 0, 3, 12]
# zeroCount = 0
# nonZeroArray = []
# for num in nums:
#     if num == 0:
#         zeroCount += 1
#     else:
#         nonZeroArray.append(num)
#         print("Nonzero", nonZeroArray)

# nums = nonZeroArray + [0] * zeroCount


# print(nums)
zeroCount = nums.count(0)
nums[:] = [i for i in nums if i != 0]
print("nums before zero", nums)
nums += [0] * zeroCount

print(nums)

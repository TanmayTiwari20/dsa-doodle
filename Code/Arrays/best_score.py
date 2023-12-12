myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
# 90 87


def firstSecond(givenList):
    # TODO
    givenList.sort(reverse=True)
    return givenList[0:2]


print(firstSecond(myList))

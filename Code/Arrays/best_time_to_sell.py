def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    left, right = 0, 1
    maxProfit = 0
    while right < len(prices):
        print("Right: ", right)
        print("left: ", left)
        currProfit = prices[right] - prices[left]
        print(f"currProfit = {prices[right]} - {prices[left]}")
        print("currProfit: ", currProfit)
        if prices[left] < prices[right]:
            maxProfit = max(currProfit, maxProfit)
            print("maxProfit: ", maxProfit)
        else:
            left += 1
        right += 1

        print("\n")
    return maxProfit


# minVal = min(prices)
# print("minVal: ", minVal)
# minValPos = prices.index(minVal)
# print("minValPos: ", minValPos)
# maxVal = max(prices[minValPos:])
# print("maxVal: ", maxVal)
# return maxVal - minVal


print(maxProfit(None, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]))

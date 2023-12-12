def move(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j += 1
    return arr


print(move([1, 0, 5, 7, -1, -2, -3],))


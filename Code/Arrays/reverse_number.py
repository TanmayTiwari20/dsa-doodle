def reverse(x):
    # x = int(input())
    x = str(x)
    x = x[::-1]
    if x[-1] == "-":
        x = x[0:-1]
        x = "-" + x
    x = int(x)
    return x


print(reverse(-123))

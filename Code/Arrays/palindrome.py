x = 51231


def palindrome(x):
    return 0 if x < 0 else str(x) == (str(x)[::-1])


print(palindrome(-121))

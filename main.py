l = int(input("Enter the value of n:"))
result = 0


def sum(n):
    if n == 1:
        return 1
    else:
        return n+sum(n-1)


result = sum(l)
print("Sum =", result)

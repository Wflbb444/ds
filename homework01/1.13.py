n=int(input())
def num(n):
    if n == 0:
        return 1
    else:
        return n * num(n - 1)
print(num(n))
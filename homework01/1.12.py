def cube(x):
    y = x
    for i in range(8):
        y = (2 * y + x / y ** 2) / 3
    return y
m=float(input())
print(cube(m))
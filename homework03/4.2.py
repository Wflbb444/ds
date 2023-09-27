from datetime import datetime

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

start_time = datetime.now()

result = fibonacci(30)

end_time = datetime.now()

print("斐波那契数列第30项的值为：", result)
print("计算用时：", end_time - start_time)
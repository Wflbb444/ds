def dec2bin(num):
    # 将十进制小数转换为整数
    xint = int(num)
    # 将小数部分转换为二进制
    xfrac = num - xint
    ans = ''
    # 将整数部分转换为二进制
    if xint == 0:
        ans = '0'
    while xint > 0:
        ans = str(xint % 2) + ans
        xint = xint // 2
    # 将小数部分转换为二进制
    ans = ans + '.'
    while xfrac > 0:
        xfrac = xfrac * 2
        ans = ans + str(int(xfrac))
        xfrac = xfrac - int(xfrac)
    return ans
x=float(input())
print(dec2bin(x))

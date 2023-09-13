import re
string1=input()
def isContinuousChar(pwd):
    # 判断是否存在有连续两个相同的字母
    #[a-zA-Z]是为了匹配单个字母
    # \\1是为了匹配与第一组内容重复的字母
    num  = len(re.findall(r"([a-z]|[A-Z]|[0-9])\1",pwd))
    if num>0:
        return True
    else:
        return False
print(isContinuousChar(string1))
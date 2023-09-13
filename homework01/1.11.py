import re
string1=input()
pattern=re.compile(r'\s+')
print(pattern.sub('',string1))
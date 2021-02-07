import re
reg1="{[^}]*}"
reg2="""(#(?:[0-9A-Fa-f]){3}|#(?:[0-9A-Fa-f]){6})[^0-9a-fA-F]"""
n=input()
s=""
for i in range(n): s+=raw_input()
x=re.findall(reg1,s)
for l in x:
    y=re.findall(reg2,l)
    #print l
    for z in y: print z
import random
import os

lch=[]
lans=[]
score=[]
hsh=[]
file=open("ask.dat",mode="r")
temp=''
tc=0
text_lines=file.readlines()
for text_line in text_lines:
    if text_line:
        if text_line=='####\n':
            lch.append(temp)
            lans.append(tc)
            temp=''
            tc=0
        else:
            temp=temp+text_line
file.close()

def lcs(a,b):
    lena=len(a)
    lenb=len(b)
    ans=0
    c=[[0 for i in range(lenb+1)] for j in range(lena+1)]
    flag=[[0 for i in range(lenb+1)] for j in range(lena+1)]
    for i in range(lena):
        for j in range(lenb):
            if a[i]==b[j]:
                c[i+1][j+1]=c[i][j]+1
            elif c[i+1][j]>c[i][j+1]:
                c[i+1][j+1]=c[i+1][j]
            else:
                c[i+1][j+1]=c[i][j+1]
            ans=max(c[i+1][j+1],ans)
    return ans

def hs(s):
    a=1
    for i in s:
        if (i>='0' and i<='9') or (i>='a' and i<='z') or (i>='A' and i<='Z'):
            a*=131
            a+=ord(i)
            a%=1000000007
    return a

n=len(lch)
file=open("score.dat",mode="r")
for i in range(len(score),n):
    score.append(int(file.readline()))
for i in lch:
    hsh.append(hs(i))
for i in range(n):
    if score[i]==30000:
        continue
    print(i)
    for j in range(i+1,n):
        if score[j]==30000:
            continue
        if hsh[i]==hsh[j]:
            score[j]=30000
            break

file=open("task.dat",mode="w+")
for i in range(n):
    if score[i]!=30000:
        file.write(lch[i])
        file.write("####\n")
file.close()
file=open("tscore.dat",mode="w+")
for i in range(n):
    if score[i]!=30000:
        file.write("%d\n"%(score[i]))
file.close()

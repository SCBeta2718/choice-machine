import random
import os

lch=[]
lans=[]
score=[]
file=open("qaa.txt",mode="r")
temp=''
tc=0
text_lines=file.readlines()
for text_line in text_lines:
    if text_line:
        if text_line=='########\n':
            lch.append(temp)
            lans.append(tc)
            temp=''
            tc=0
        elif text_line.find("Answer: ")!=-1:
            for i in text_line:
                if(ord(i)>=ord('A') and ord(i)<=ord('Z')):
                    tc+=(1<<(ord(i)-ord('A')))
                if(ord(i)>=ord('a') and ord(i)<=ord('z')):
                    tc+=(1<<(ord(i)-ord('a')))
            temp=temp+text_line
        else:
            # continue
    else:
        break
file.close()

n=len(lch)
try:
    file=open("score.dat",mode="r")
    text_lines=file.readlines()
    for text_line in text_lines:
        score.append(int(text_line))
    file.close
finally:
    for i in range(len(score),n):
        score.append(0)
    while True:
        os.system("clear")

        cnt=0
        dict={}
        for i in score:
            if i<1:
                cnt+=1
                if i in dict:
                    dict[i]+=1
                else:
                    dict[i]=1
        keys=sorted(dict)

        print("目前剩余比例：%4f"%(cnt/n))
        print("\n")
        # print("分值分布：")
        # for k in keys:
        #     print("%4d"%(k),end=": ")
        #     print("%4d"%(dict[k]))
        
        tm=random.randint(1,cnt)
        m=0
        for i in range(n):
            if score[i]<1:
                tm-=1
            if tm==0:
                m=i
                break
        print("\n")

        tp=0
        for i in range(32):
            if((lans[m]&(1<<i))):
                tp+=1
        if tp>1:
            print("多选题")
        else:
            print("单选题")

        print(lch[m])
        print("请输入答案：")

        ttc=0
        tans=input()
        for i in tans:
            if(ord(i)>=ord('A') and ord(i)<=ord('Z')):
                ttc|=(1<<(ord(i)-ord('A')))
            if(ord(i)>=ord('a') and ord(i)<=ord('z')):
                ttc|=(1<<(ord(i)-ord('a')))


        f=True
        for i in range(32):
            if((ttc&(1<<i))!=(lans[m]&(1<<i))):
                f=False
                break
        
        if f:
            print("\033[0;32m正确！\033[0m")
            if score[m]>=0:
                score[m]+=1
            else:
                score[m]=(score[m]+1)//2
        else:
            print("\033[0;31m错误！\033[0m")
        
        print("\n")
        print("你的答案：",end="")
        for i in range(32):
            if((lans[m]&(1<<i)) and (ttc&(1<<i))):
                print("\033[0;32m%c\033[0m"%chr(ord('A')+i),end='')
            elif((lans[m]&(1<<i)) and not (ttc&(1<<i))):
                print(" ",end='')
            elif(not (lans[m]&(1<<i)) and (ttc&(1<<i))):
                print("\033[0;31m%c\033[0m"%chr(ord('A')+i),end='')
            else:
                continue
        print("")
        print("标准答案：",end="")
        for i in range(32):
            if((lans[m]&(1<<i)) and (ttc&(1<<i))):
                print("\033[0;32m%c\033[0m"%chr(ord('A')+i),end='')
            elif(not (lans[m]&(1<<i)) and (ttc&(1<<i))):
                print(" ",end='')
            elif((lans[m]&(1<<i)) and not (ttc&(1<<i))):
                print("\033[0;31m%c\033[0m"%chr(ord('A')+i),end='')
            else:
                continue
        print("")

        tf=input("按任意键继续，按 F 退出：")
        if tf=='f' or tf=='F':
            file=open("score.dat",mode="w+")
            for i in score:
                file.write(str(i)+"\n")
            file.close()
            break
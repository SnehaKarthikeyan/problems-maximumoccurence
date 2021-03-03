Coding:

a=int(input())
b=list(map(int,input().split()))
t=[]
for i in b:
    t.append(b.count(i))
    p=max(t)
for i in b:
    if(b.count(i)==p):
     print(i,end='')
     break

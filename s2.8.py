a,b= map(int,input().split())
for k in range(a+1,b):
    s=0
    temp=k
    while(temp>0):
        f=temp%10
        s+=f**3
        temp//=10
    if(k==s):
        print(k,end=" ")

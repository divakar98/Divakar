a = int(input())
v = input()[::-1]
vo=('a','e','i','o','u','A','E','I','O','U')
for i in v:
    if i in vo:
        v=v.replace(i,"")
print(v,end="")

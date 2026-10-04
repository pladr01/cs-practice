porog=float(input())
n=int(input())
kerror=0
knoterror=0
kprporog=0
maxt=-99999999999
sum=0
for i in range(n):
    a=input()
    if a=="error":
        kerror+=1
    else:
        a=float(a)
        if a>porog:
            kprporog+=1
        if a>maxt:
            maxt=a
        knoterror+=1
        sum+=a
sr=sum/knoterror
print(n)
print(kerror)
print(kprporog)
print(f"{maxt:.1f}")
print(f"{sr:.1f}")



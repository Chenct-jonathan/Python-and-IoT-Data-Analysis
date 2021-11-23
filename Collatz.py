c0=int(input("input any integer:"))
step=0
while c0!=1:
    print(c0)
    step+=1
    if (c0%2==0):
        c0=int(c0/2)
    else:
        c0=int(c0*3+1)
        
print(c0)
print("step=",step)

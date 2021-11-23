s=input("space between rows:")
Su = s.split()

square=[]
def check(x):
    return ''.join(sorted(x)) == "123456789"

isSudoku = True
for i in range (0,9,1):
    isSudoku = isSudoku and check(s[i])
    if (not isSudoku):break

if (isSudoku):
    for k in range (0,9,1):
        
        isSudoku = isSudoku and check([s[i][k] for i in range(9)])
        if (not isSudoku):break  


if (isSudoku):
    for y in range (0,7,3):
        for x in range (0,7,3):
            for i in range (0,3,1):      
                for j in range (0,3,1):
                    square.append(s[j+x][i+y])           
            isSudoku = isSudoku and check(square)
            if (not isSudoku):break
            square.clear()
            
                        
                    
        
if (isSudoku == True):
    print ("Yes")
else:
    print("No")

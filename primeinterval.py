inp=raw_input().split()                                             
sr = int(inp[0])
er = int(inp[1])
for num in range(sr+1,er):
    if num>1:
        for i in range (2,num):
            if (num%i)==0:
                break
        else:
            print num,

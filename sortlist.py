n = int(input())
l = []
l=input().split()
for i in range (len(l)):
    l[i]=int(l[i])
l.sort()
print(*l,sep=' ')
        

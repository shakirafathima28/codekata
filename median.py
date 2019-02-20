n = int (input())
l = []
l=input().split()
for i in range (len(l)):
    l[i]=int(l[i])
l.sort()
length = len(l)
if (length % 2 == 0):
    median = (l[(length)//2] + l[(length)//2-1]) / 2
else:
    median = l[(length-1)//2]
 
print(median)

N=int(raw_input())
sum=0
order=len(str(N))
temp=N
while temp > 0 :
    digit = temp % 10
    sum += digit**order
    temp//=10
if N==sum:
    print("yes")
else:
    print("no")

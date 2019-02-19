inp = raw_input().split()
sr = int(inp[0])
er = int(inp[1])
for N in range (sr,er):
    sum=0
    order=len(str(N))
    temp=N
    while temp > 0 :
        digit = temp % 10
        sum += digit**order
        temp//=10
        if N==sum:
            print N,

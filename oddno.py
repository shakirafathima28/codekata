inp=raw_input().split()
sr = int(inp[0])
er = int(inp[1])
for num in range(sr,er+1):
    if num%2==1:
        print num,

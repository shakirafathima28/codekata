inp=raw_input().split()
sr = int(inp[0])
er = int(inp[1])
for num in range(sr+1,er):
    if num%2 == 0:
        print num,

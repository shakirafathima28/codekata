inp=raw_input().split()
number = int(inp[0])
exponent = int(inp[1])
power = 1
for i in range(1, exponent + 1):
    power = power * number
print(power)

inp= raw_input().split()
n = int(inp[0])
a = int(inp[1])
d = int(inp[2])
def main(n,a,d):
    return (n * (2 * a + (n - 1) * d)) / 2
print(main(n,a,d))

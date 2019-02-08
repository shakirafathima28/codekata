inputValue = raw_input()
a,b,c = inputValue.split(" ")
if((a>b) and (a>c)):
    print(a)
elif((b>a) and (b>c)):
    print(b)
elif((c>a) and (c>b)):
    print(c)

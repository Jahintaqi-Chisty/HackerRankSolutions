n = int(input())
for i in range(0,n):
    s = str(input())
    a = ""
    b = ""

    for i in range(0,len(s)):
        if i%2 == 0 or i == 0:
            a = a+s[i]
        else:
            b= b+s[i]

    print(a+" "+b)


# b = 0x10
# a = int(str(b),16) 这里传的值是 str的0x16所以最终结果变成22
# a = int('0x10',16)
# print(a)

# b = 10
# a = int(str(b),16)
# print(a)

def gcd(a,b):
    if b == 0:
        return a
    elif a > b:
        return gcd(b,a%b)
    else:
        return gcd(a,b%a)

# print(gcd(60,24))

# 58^12 * x = 1 mod 71
#
#
# a = 19**3 %71
# print(a)





c,d = divmod(58**12,71)
print(c,d)
for i in range(1,71,1):
    if i*d%71 == 1:
        print(i)
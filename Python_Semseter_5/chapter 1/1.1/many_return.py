#wap to return sum , diff , prod and quotient in a simgle function

def calc(a,b):
    s=a+b
    d=a-b
    p=a*b
    q=a/b
    return a,d,p,q

# s,d,p,q=calc(10,5)
# print(d)
# print(type(d))

d=calc(10,5)
print(d)
print(type(d))
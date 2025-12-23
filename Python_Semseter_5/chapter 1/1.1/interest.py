def sInterest(p,t,r):
    return (p*t*r)/100

def cInterest(p,t,r):
    return p*(((1+r/100)**t)-1)

if __name__=="__main__":
    p=float(input('p= '))
    t=float(input('t= '))
    r=float(input('r= '))
    print(f'Simple Interest is {sInterest(p,t,r):.3f}')
    print(f'Compound Interest is {cInterest(p,t,r):.3f}')
import sys

print("hello")
print(sys.argv)
n1=float(sys.argv[1])
n2=float(sys.argv[2])
sys.argv[1]=n1+n2
print(sys.argv[1])
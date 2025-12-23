import pdb
x=[1,2,3,4]
pdb.set_trace()
# used to debug the code line wise line so that we can know what part of the code is giving error.

for i in range(100):
    y = x.pop()
    print(y)
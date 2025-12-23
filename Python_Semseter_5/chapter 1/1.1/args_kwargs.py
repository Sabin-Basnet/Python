# #using args we can define any number of arguments at run time

# def avg(*args):
#     s=0
#     for i in args:
#         s=s+i
#         return s/len(args)
    
# print(avg(1,2,3,4,5))

# def func(**kwargs):
#     for item in kwargs.items():
#         print(item)

# func(name="ram", address="dharan")

def func(*args,**kwargs):
    print(args)
    print(kwargs)


func(1,2, a=10, b=20)
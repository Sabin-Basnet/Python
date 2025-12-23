#wap to create a class named distance that has feet and 
# inch as data members. Overload any 2 operators.

class Distance:
    def __init__(self,feet,inch):
        self.feet=feet
        self.inch=inch
        self.normalize()

    def normalize(self):
        self.feet +=self.inch//12
        self.inch=self.inch%12

    # Operator overloading +
    def __add__(self, other):
        f = self.feet + other.feet
        i = self.inch + other.inch
        return Distance(f, i)

    # Operator overloading  ==
    def __eq__(self, other):
        return self.feet == other.feet and self.inch == other.inch

    def display(self):
        print(f"{self.feet} feet {self.inch} inch")

    #operator overloading -
    def __sub__(self,other):

        # f=self.feet - other.feet
        # i=self.inch - other.inch
        # return Distance(f,i)
        t1=self.feet *12 +self.inch
        t2=other.feet * 12 + other.inch
        return Distance(0,t1-t2)
        # print(f"t1={t1} and t2={t2}")



d1 = Distance(5, 5)
d2 = Distance(5, 6)

d3 = d1 + d2
print("After addition:")
d3.display()

print("Are d1 and d2 equal?", d1 == d2)

d3=d1-d2
print("After Substraction:")
d3.display()

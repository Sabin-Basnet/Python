class DataSample:
    def __init__(self, name, values):
        self.name = name
        self.values = list(values)

    def normalize(self):
        max_val= max(self.values)
        self.values = [x/max_val for x in self.values]

    def plot(self):
        import matplotlib.pyplot as plt
        plt.plot(self.values, marker='o')
        plt.title(self.name)
        plt.show()

    def summary(self):
        return{
            "mean": sum(self.values)/len(self.values),
            "max": max(self.values),
            "min": min(self.values),
            "range": max(self.values) - min(self.values),
        }

    def display(self):
        print(f"Data Sample: {self.name}")
        print("Values:", self.values)
        DataSample.summary(self)
        DataSample.normalize(self)
        DataSample.plot(self)
        
    
samples=[
    DataSample("Sample1", [1,2,3,4,5]),
    DataSample("Sample2", [10,20,30,40,50]),
    DataSample("Sample3", [5,15,25,35,45])
]

for s in samples:
    print(s.name, s.summary())
    s.display()


    
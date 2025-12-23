import data_utils as du
from data_sample import DataSample
# import data_sample as ds

data=[10, 20, 30, 40]
print("Mean:", du.mean(data))
print("Max:", du.max_value(data))
print("Min:", du.min_value(data))

obj = DataSample("Obj1", data)
obj.display()

# obj.summary()
# samples=[
#     ds.DataSample("Sample1", [1,2,3,4,5]),
#     ds.DataSample("Sample2", [10,20,30,40,50]),
#     ds.DataSample("Sample3", [5,15,25,35,45])
# ]
# for s in samples:
#     print(s.name, s.summary())


samples = [
    DataSample("SampleA", [5, 15, 25]),
    DataSample("SampleB", [10, 20, 30])
]

for s in samples:
    s.display()
    print(s.summary())
    s.plot()

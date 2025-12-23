from data_sample import DataSample


# Expose a small collection and the class for convenience
data_samples = [
	DataSample("Sample1", [1, 2, 3, 4, 5]),
	DataSample("Sample2", [10, 20, 30, 40, 50]),
]

__all__ = ["DataSample", "data_samples"]

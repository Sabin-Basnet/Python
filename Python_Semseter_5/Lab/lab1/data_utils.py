def mean(lst):
    """Return the mean of a non-empty list of numbers."""
    if not lst:
        raise ValueError("mean() requires a non-empty list")
    return sum(lst) / len(lst)


def max_value(lst):
    if not lst:
        raise ValueError("max_value() requires a non-empty list")
    return max(lst)


def min_value(lst):
    if not lst:
        raise ValueError("min_value() requires a non-empty list")
    return min(lst)


def data_range(lst):
    if not lst:
        raise ValueError("data_range() requires a non-empty list")
    return max(lst) - min(lst)


def variance(lst):
    if not lst:
        raise ValueError("variance() requires a non-empty list")
    m = sum(lst) / len(lst)
    return sum((x - m) ** 2 for x in lst) / len(lst)


def stddev(lst):
    return variance(lst) ** 0.5


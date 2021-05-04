def mean(numbers):
    """Compute the arithmetic mean of the values in numbers."""
    # add the numbers together
    s = sum(numbers)
    # count the values in numbers
    N = len(numbers)
    # compute the arithmetic mean
    mean = s / N
    return mean

# create a list of numbers
numbers_one = [1, 3, 5, 7]
# calculate the mean
numbers_one_mean = mean(numbers_one)
print(f"Mean: {numbers_one_mean}")

# create a list of numbers
numbers_two = [2, 4, 6, 8]
# calculate the mean
numbers_two_mean = mean(numbers_two)
print(f"Mean: {numbers_two_mean}")

# TODO: fill in the program's output
# Mean: 4.0
# Mean: 5.0

from rich import print
from rich import inspect

def mean(numbers):
    # add the numbers together
    numbers_sum = sum(numbers)
    # count how many values are in numbers
    numbers_count = len(numbers)
    # compute the arithmetic mean
    arithmetic_mean = numbers_sum / numbers_count
    return arithmetic_mean

# create a list of numbers
numbers_one = [1, 3, 5, 7]
# display a message and a magnifying glass emoji
print("Inspecting the list! :mag_right:")
# inspect the list of numbers
inspect(numbers_one, methods=True)
# display a message and a rocket emoji
print("Computing the mean! :rocket:")
# calculate the mean and display it
numbers_one_mean = mean(numbers_one)
print(f"Mean: {numbers_one_mean}")

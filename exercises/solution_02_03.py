def mean(numbers):
    # add the numbers together
    number_sum = sum(numbers)
    # count the values in numbers
    number_count = len(numbers)
    # compute the arithmetic mean
    arithmetic_mean = number_sum / number_count
    return arithmetic_mean

def display(numbers):
    comma = ", "
    return comma.join(map(str, numbers))

# create a list of numbers
numbers_one = [1, 3, 5, 7]
# create the text of the list to display
numbers_one_text = display(numbers_one)
print(f"Values: {numbers_one_text}")
# calculate the mean
numbers_one_mean = mean(numbers_one)
print(f"Mean: {numbers_one_mean}")

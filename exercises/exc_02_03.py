def mean(numbers):
    # add the numbers together
    number_sum = sum(numbers)
    # count how many values are in numbers
    number_count = len(numbers)
    # compute the arithmetic mean
    arithmetic_mean = number_sum / number_count
    return arithmetic_mean

def display(numbers):
    comma = ", "
    return comma.join(map(str, numbers))

# create a list of numbers
numbers_one = [1, 3, 5, 7]
# TODO: create text of the list to display
numbers_one_text = ______(numbers_one)
print(f"Values: {________________}")
# TODO: calculate and display the mean
numbers_one_mean = ____(numbers_one)
print(f"Mean: {________________}")

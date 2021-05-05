def mean(numbers):
    # add the numbers together
    number_sum = sum(numbers)
    # count how many values are in numbers
    number_count = len(numbers)
    # compute the arithmetic mean
    arithmetic_mean = number_sum / number_count
    return arithmetic_mean

def display(numbers):
    # create a comma separate for text
    comma = ", "
    # create and return a display of numbers
    # separated by comma, like "1, 3, 5, 7"
    return comma.join(map(str, numbers))

# create a list of numbers
numbers_one = [1, 3, 5, 7]
# create the text of the list to display
numbers_one_text = display(numbers_one)
print(f"Values: {numbers_one_text}")
# calculate the mean
numbers_one_mean = mean(numbers_one)
print(f"Mean: {numbers_one_mean}")

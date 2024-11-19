# import pdb; pdb.set_trace()

def remove_negatives(numbers):
    return [number for number in numbers if number >= 0]
# When you remove an element during iteration, the indexes shift, which can cause some negative numbers to be skipped.

numbers_list = [1, -2, 3, -4, -5, 6, -7, -8]
print(remove_negatives(numbers_list))  # Expected: [1, 3, 6]

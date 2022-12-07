import re
import os.path
import sys

# Remove duplicates from a sorted array.
def remove_duplicates(arr):
    # Iterating backwards as the length of the array is changing.
    for i in range(len(arr)-1, 0, -1):
        if arr[i] == arr[i-1]:
            del arr[i]
    return arr

# Setup variables for future computation.
filepath = 'Resources\\Rucksack_Reorganization.txt'
sum_of_items = 0

# Check that file exists, if not exit with error message.
if not os.path.isfile(filepath):
    sys.exit("Error - File not found.")

# Open file and read it in line by line.
file = open(filepath, "r")
lines = file.readlines()

for line in lines:
    line_length = len(line)
    # Divide the rucksack in half.
    first_half = line[0:int(line_length/2)].strip()
    second_half = line[int(line_length/2):line_length].strip()
    # Put those halfs into sorted arrays and remove duplicate values.
    rucksack_one = remove_duplicates(sorted([c for c in first_half]))
    rucksack_two = remove_duplicates(sorted([c for c in second_half]))
    # Compare the values of the first rucksack to the second and add its value to the sum.
    for item_r2 in rucksack_two:
        for item_r1 in rucksack_one:
            if item_r1 == item_r2:
                # Calculate lower case values.
                if re.search('[a-z]', item_r1):
                    sum_of_items += (ord(item_r1) - 96)
                # Calculate upper case values.
                if re.search('[A-Z]', item_r1):
                    sum_of_items += (ord(item_r1) - 38)

file.close()

# Print out solution.
print(f'Sum of the items: {sum_of_items}')

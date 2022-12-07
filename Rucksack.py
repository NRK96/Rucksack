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

# Solution for Day 3, Part 1.
def part_1_solution(l, sum):
    line_length = len(l)
    # Divide the rucksack in half.
    first_half = l[0:int(line_length/2)].strip()
    second_half = l[int(line_length/2):line_length].strip()
    # Put those halfs into sorted arrays and remove duplicate values.
    rucksack_one = remove_duplicates(sorted([c for c in first_half]))
    rucksack_two = remove_duplicates(sorted([c for c in second_half]))
    # Compare the values of the first rucksack to the second and add its value to the sum.
    for item_r2 in rucksack_two:
        for item_r1 in rucksack_one:
            if item_r1 == item_r2:
                # Calculate lower case values.
                if re.search('[a-z]', item_r1):
                    sum += (ord(item_r1) - 96)
                # Calculate upper case values.
                if re.search('[A-Z]', item_r1):
                    sum += (ord(item_r1) - 38)
    return sum

# Setup variables for future computation.
filepath = 'Resources\\Rucksack_Reorganization.txt'
sum_of_items_part_one = 0
sum_of_items_part_two = 0
group_count = 0
group_line_one = ''
group_line_two = ''
group_line_three = ''

# Check that file exists, if not exit with error message.
if not os.path.isfile(filepath):
    sys.exit("Error - File not found.")

# Open file and read it in line by line.
file = open(filepath, "r")
lines = file.readlines()

for line in lines:
    # Part 1
    sum_of_items_part_one = part_1_solution(line, sum_of_items_part_one)
    # Part 2
    group_count += 1
    # Keep track of past lines for the "Elf Groups"
    if group_count == 1:
        group_line_one = line.strip()
    if group_count == 2:
        group_line_two = line.strip()
    if group_count == 3:
        group_line_three = line.strip()
        # Put those lines into sorted arrays and remove duplicate values.
        rucksack_one = remove_duplicates(sorted([c for c in group_line_one]))
        rucksack_two = remove_duplicates(sorted([c for c in group_line_two]))
        rucksack_three = remove_duplicates(sorted([c for c in group_line_three]))
        # Compare the values of the first, second and third rucksacks and add their value to the sum if they match.
        for item_r3 in rucksack_three:
            for item_r2 in rucksack_two:
                for item_r1 in rucksack_one:
                    if item_r3 == item_r2 == item_r1:
                        # Calculate lower case values.
                        if re.search('[a-z]', item_r1):
                            sum_of_items_part_two += (ord(item_r1) - 96)
                        # Calculate upper case values.
                        if re.search('[A-Z]', item_r1):
                            sum_of_items_part_two += (ord(item_r1) - 38)
        group_count = 0

file.close()

# Print out solution.
print(f'Sum of the items (Part 1): {sum_of_items_part_one}')
print(f'Sum of the items (Part 2): {sum_of_items_part_two}')

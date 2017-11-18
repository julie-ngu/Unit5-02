# Created by: Julie Nguyen
# Created on: Nov 2017
# Created for: ICS3U
# This program makes an array of 10 random numbers from 1 to 10 and then finds the largest value of these 
# numbers

from numpy import random

def find_max_value(array = []):
    # finds max value in array
    
    max_number = array[0]
    
    for single_number in array:
        if max_number < single_number:
            max_number = single_number
            
    return max_number

# input
counter = 0
random_numbers = []

while counter < 10:
    single_number = random.randint(1, 10 + 1)
    print(single_number)
    random_numbers.append(single_number)
    counter = counter + 1
        

# process
largest_value = find_max_value(random_numbers)

# output
print("\nThe maximum value of the array is " + str(largest_value) + ".\n")

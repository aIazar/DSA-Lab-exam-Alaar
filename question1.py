'''Write a python program that allows the user to enter a sequence of numbers into an 
array. The program should then prompt the user to enter a number to be 
searched. The program should determine if the number is present in the array 
and, if so, display the number of times it appears.'''


def num_frquency(arr, num):
    count = 0
    for element in arr:
        if element == num:
            count += 1
    return count
sequence = input("Enter a sequence of numbers separated by space: ")
numbers = sequence.split()
array = [int(num) for num in numbers]
target = int(input("Enter the number you want to search: "))
frequency = num_frquency(array, target)
if frequency == 0:
    print("The number", target, "is not found in the array.")
else:
    print("Number", target, "appears", frequency, "time in the array.")





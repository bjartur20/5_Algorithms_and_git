'''
1. Takes some input (positive int) from the user.
2. Stores the largest number which the user types in.
3. Stops asking for input when the user inputs a negative number.
4. Prints the largest number.
'''

#Bjartur Thorhallsson

number = int(input("Input a number: "))
largest_number = 0
while number >= 0:
    if number > largest_number:
        largest_number = number
    number = int(input("Input a number: "))
print(largest_number)
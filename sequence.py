'''
The sequance is  difined as the sum of the last three numbers
1. Input from the user which decides how many numbers in the sequance should be printed.
2. 

'''

nr_of_sequences = int(input("How many numbers do you want: "))

first_nr = 1
second_nr = 2
third_nr =  3

for x in range(1, nr_of_sequences+1):
    if x <= 3:
        print(x)
    else:
        nr = first_nr+second_nr+third_nr
        first_nr, second_nr, third_nr = second_nr, third_nr, nr
        print(nr)
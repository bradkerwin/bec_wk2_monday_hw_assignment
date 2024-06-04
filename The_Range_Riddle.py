# Task 1: Every Other Day Write a program that prints each day of the week, but only if that day is on an even index.

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for x in range(len(days_of_week)): # This ranges through the length of the list, which is 6 because there are 6 items. It starts from 0 and ends at 6.
    if x % 2 == 0:  # Creates a condition of the index is even.
        print(days_of_week[x])  # Prints out the items in the list with an even numbered index.
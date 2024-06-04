# Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true (an infinite loop). Ask the user a question until their answer triggers a break statement (hint: use an if statement to evaluate their answer).

while True:
    user_input = input("What's your favorite band? ") # Asks the user to give their input.
    if user_input == "green day":
         print("That's right! They're awesome!") 
         break # The loop will break once the user enters the input 'green day'.
    else:
         print("Nope! Try again!") # This will keep repeating no matter what input the user gives until they input the answer 'green day'.

# Task 2: Conditional Exit Create a while loop that will terminate after 5 iterations, and each iteration you print which iteration it is on. (use a control variable)

count = 0
while count <= 4: # Will repeat until it iterates through the list 5 times, then will automatically break
    print('Another one')
    count += 1  # Adds 1 to the count for each iteration.
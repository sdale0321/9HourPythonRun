import random

top_of_range = input("Type a number: ") #needs int conversion

if top_of_range.isdigit():
    top_of_range = int(top_of_range) #top_of_range is converted here 

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else: 
    print('Please type a number next time.')
    quit() 

random_number = random.randint(0, top_of_range)
guesses = 0

while True: #This block of code will run until it executes the section that includes the break command 
    guesses += 1
    user_guess = input("Make a guess; ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else: 
        print('Please type a number next time.')
        continue #automatically brings you back to the top of the loop -> different than break, and keeps this section of code running til user input is correct 

    if user_guess == random_number: #covering the scenario that the user guesses correctly: 
        print("You got it!")
        break #Here the whole while loop is broken and the next code past this loop is ran (line 36)
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses") #the print statement is smart enough to convert values like "guesses", an int, into a str.  
                                            # the commas add spaces as well, like you would in normal concatenation 
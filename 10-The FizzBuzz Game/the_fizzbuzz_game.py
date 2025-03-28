print("Welcome to the FizzBuzz Game Challenge! 🥂🐝")

# User input to define the range
end_number = int(input("Please enter the maximum number for the FizzBuzz range: \n"))

# Loop based on user input
for number in range(1, end_number + 1):  
    if number % 3 == 0 and number % 5 == 0:  # Divisible by both 3 and 5
        print("FizzBuzz 🥂🐝")
    elif number % 3 == 0:                    # Divisible by 3
        print("Fizz🥂")
    elif number % 5 == 0:                    # Divisible by 5
        print("Buzz🐝")
    else:
        print(number)    # If none of the conditions are met, print the number.

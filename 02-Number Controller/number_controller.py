print("Welcome to the Number Controller! 🔢")

# Number input from user
number_to_check = int(input("Enter a number to check if it's Even or Odd: \n"))  

# Check if the number is even or odd
if number_to_check % 2 == 0:       
   print(f"{number_to_check} is an Even number! ✅")   
else:
   print(f"{number_to_check} is an Odd number! 🔴")

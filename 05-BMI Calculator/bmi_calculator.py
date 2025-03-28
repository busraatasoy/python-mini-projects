print("Welcome to the BMI Calculator! 🧮")

# Height input from user
height = float(input("What is your height in cm? \n"))

# Weight input from user
weight = float(input("What is your weight in kg? \n"))


# Calculate the bmi using weight and height.
bmi = weight / ((height / 100) ** 2)  # Convert cm to meters

# Check if you are in bmi standard
if bmi >= 25 :
    print("You are overweight. Consider a balanced diet & regular exercise. 🏃‍♂️")
elif bmi >= 18.5:
    print("You have a normal weight. Keep up the good work! 👍")
else:
    print(" You are underweight. A nutritious diet might help! 🍎")

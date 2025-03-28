print("Welcome to the Roller Coaster!🎢🎡")

# Height input from user
height = int(input("What is your height in cm? \n"))  

#Calculate the bill
bill = 0  

if height >= 120:  # Check height for rollercoaster
    print("You can ride the Roller Coaster!✅")
 
    # Age input from user
    age = int(input("What is your age? \n"))  

    if age <= 12: 
        bill = 5
        print("Child (0-12) tickets are 💲5.")  
    elif age <= 18: 
        bill = 7
        print("Youth(13-18) tickets are 💲7.")  
    elif age >= 45 and age <= 55:         # Midlife crisis condition
        print("Everything is going to be ok. Your ticket is free. Have a free ride on us!")  
    else:                                  
        bill = 12
        print("Adult(19+) or not in midlife crisis tickets are 💲12.")
  
    # Ask if the user wants a photo.
    wants_photo = input("Do you want to have a photo taken📷? Type y for Yes and n for No. ")
    
    if wants_photo.lower() == "y":  # If the user wants a photo.
        bill += 3  # Add $3 to the bill for the photo.

    # Final bill
    print(f"Your final bill is 💲{bill}")  

else:
# If the height condition is not met.
    print("Sorry, you need to be a bit taller to ride! 🙅‍♀🔴")  

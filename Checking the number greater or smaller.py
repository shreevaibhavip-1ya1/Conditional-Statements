user_number = float(input("Enter your number: "))

# Checking the condition of the greater and smaller than number
if user_number > 15:
    # This block executes if the number is greater than 15
    print("I am a greater number")
    print("I'am in if block")
    print("I'am not in else and i'am in if block")
else:
    # This block executes if the number is 15 or smaller
    print("I am smaller than 15")
    print("I'am in else block")
    print("I'am not in else block and not in the if block")

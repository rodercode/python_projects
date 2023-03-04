# Variables
tip = 0

# Greet user
print("Welcome to the tip calculator")

# Ask user for the total sum of the bill
while True:
    try:
        bill = float(input("What was the total bill? "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number")

# Ask user to choice between three options
while True:
    userInput = input(
        "What percentage tip would you like to give? 10, 12, or 15? ")

    if userInput == "10":
        tip = bill * 0.1
        break
    elif userInput == "12":
        tip = bill * 0.12
        break
    elif userInput == "15":
        tip = bill * 0.15
        break
    else:
        print("Invalid input. Please enter 10, 12 or 15")

# Calculate the total sum to pay
sum = tip + bill

# Ask user how many people should split the bill
while True:
    try:
        people = int(input("How many people to split the bill? "))
        if people < 1:
            print("Invalid input. Please enter a number greater than 0")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number")

# Calculate sum every person should pay
each_pay = round(sum / people, 2)

# Display final result
print(f"Each Person should pay: ${each_pay}")

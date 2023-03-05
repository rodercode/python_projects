# Variables
want_photo = False

# functions


def calculate_ride_cost(age, want_photo):
    sum = 0

    if age > 18:
        sum += 12
    elif age > 11 and age < 19:
        sum += 7
    else:
        sum += 5

    if want_photo == True:
        sum += 3

    return sum


# Print out Greetings
print("Welcome to the rollercoaster")

# Ask User for their height
while True:
    try:
        height = int(input("What is your height in cm? "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number")

# check customer's height
if height > 120:
    print("You can ride this rollercoaster")

    # ask customer for their age
    while True:
        try:
            age = int(input("What is your age? "))
            break
        except ValueError:
            print("Invalid input. Please enter a vaild number")

    while True:
        # ask customer for a photo
        answer = input("Do you want a photo? ").lower()

        # check if customer answer yes or no
        if answer == "yes":
            want_photo = True
            break

        elif answer == "no":
            want_photo = False
            break
        else:
            print("Invalid input. Please enter yes or no")

    # calculate the total cost of the ride
    ride_cost = calculate_ride_cost(age, want_photo)

    # Print out the total cost
    print(f"The cost of the ride will be {ride_cost}$")

else:
    print("You can't ride this rollercoaster")

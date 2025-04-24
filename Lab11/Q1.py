while True:
    try:
        s = int(input("Please enter an integer: "))
        print("You entered the integer:",s)
        break
    except ValueError:
        print("Error: That is not an integer. Please try again.")
number = int(input("Hey stranger, what is you lucky number?"))


num = int(input("Hey stranger, gimme a number to check."))
check = int(input("Hey stranger, gimme a number to divide by."))

if number % 4 == 0:
    print("Your lucky number is a multiple of number 4")
elif number % 2 == 0:
    print("Your lucky number is an even number.")
else:
    print("Your lucky number is an uneven number.")

if num % check == 0:
    print("Number is evenly divided!")
else: 
    print("Number is unevenly divided!")
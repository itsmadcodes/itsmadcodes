# The code below calculates in what year the person will turn 100y/o based upon its input 
name = input("Hey what is your name?")
age = input("And what is your age?")
age = int(age)

# Same code as age var to manipulate the string into an integer, but written more compact.
copies = int(input("What is your favorite number?"))

years_till_100 = 100 - age
year_turning_100 = 2021 + years_till_100

full_text = ("Hey, " + name + ". You will turn 100 in " + str(year_turning_100) + ".\n")
print(full_text * copies)
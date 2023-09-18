docstring = """
Hello, This is a program to calculate your weekly, monthly and annual wages based on the hourly wage you have.
To start, please enter your name
Then enter your hourly wage without the $ or £ symbols and in price format.

Then enter whether you wish to use Dollars (d) or Pounds (p)

The program will then calculate your weekly, monthly and annual wages

Thanks for using this program, the program was designed and coded with 💚 by Kieran Triggs, Software Engineer & Python Developer.
"""
print(docstring)

# input is requested from the user:

print("Hello, what is your name?")
name = input("> ")

name = name.lower()

print(f"Name: {name}")

print("What is your hourly wage?")
wage = float(input("> "))

print("What do you want to use? d for dollars, p for pounds")

dollar_pounds = input("> ")

dollar_pounds = dollar_pounds.lower()

print(f"Here are your results, {name}")


# Function to print a list of strings in a formatted box:

def printBox(wageList):
    # Calculate the maximum length of any string in the list:
    maxLength = max([len(string) for string in wageList])

    # Print the top border of the box:
    top = "-" * (maxLength + 8)
    print("+" + top + "+")
    
    # Print each string in the list, centered in the box:
    for string in wageList:
        print(f"| {string.center(maxLength + 4)}   |")

    # Print the bottom border of the box:
    bottom = "-" * (maxLength + 8)
    print("+" + bottom + "+")


# Function to calculate wage:

def calculateWage():
    if dollar_pounds == 'p':
    
        hourlyWage = f"Your Hourly Wage: £{wage:.2f} Hourly"
        
        wage_per_week = wage * 7

        weeklyWage = f"Your Weekly Wage: £{wage_per_week:.2f} Weekly"
        
        wage_per_month = wage_per_week * 4

        monthlyWage = f"Your Monthly Wage: £{wage_per_month:.2f} Monthly"
        
        wage_per_year = wage_per_month * 12

        annualWage = f"Your Annual Wage: £{wage_per_year:.2f} Annually"

        # Create a list of strings containing the hourly wage, weekly wage, monthly wage, and annual wage:
        wageList = [hourlyWage, weeklyWage, monthlyWage, annualWage]

        # Call the printBox() function to print out the list of strings in a formatted box:
        printBox(wageList)
        
    elif dollar_pounds  == 'd':
        hourlyWage = f"Your Hourly Wage: ${wage:.2f} Hourly"
        
        wage_per_week = wage * 7

        weeklyWage = f"Your Weekly Wage: ${wage_per_week:.2f} Weekly"
        
        wage_per_month = wage_per_week * 4

        monthlyWage = f"Your Monthly Wage: ${wage_per_month:.2f} Monthly"
        
        wage_per_year = wage_per_month * 12

        annualWage = f"Your Annual Wage: ${wage_per_year:.2f} Annually"

        # Create a list of strings containing the hourly wage, weekly wage, monthly wage, and annual wage:
        wageList = [hourlyWage, weeklyWage, monthlyWage, annualWage]

        # Call the printBox() function to print out the list of strings in a formatted box:
        printBox(wageList)


calculateWage()
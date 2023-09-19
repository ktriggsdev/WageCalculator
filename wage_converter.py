docstring = """
Hello, This is a program to calculate your weekly, monthly and annual wages based on the hourly wage you have.
To start, please enter your name
Then enter your hourly wage without the $ or £ symbols and in price format.

Next enter your starting wage type: hourly (h), weekly (w), monthly (m) or annually (a)

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

# input is requested from the user

print("What is your starting wage Type: hourly (h), weekly (w), monthly (m) or annually (a)")
starting_wage = input("> ")

starting_wage = starting_wage.lower()

# Function to get input from the user on whether to use dollars or pounds:

def dollarsOrPounds():
    print("What do you want to use? d for dollars, p for pounds")

    global dollar_pounds
    
    dollar_pounds = input("> ")

    dollar_pounds = dollar_pounds.lower()

# Function to get input from the user on what their hourly wage is:
    
def wagePerHour():
    print("What is your hourly wage?")
    global wage_hour
    wage_hour = float(input("> "))
    return wage_hour

# Function to get input from the user on what their weekly wage is:    
    
def wagePerWeek():
    print("What is your Weekly wage?")
    global wage_week
    wage_week = float(input("> "))
    return wage_week

# Function to get input from the user on what their monthly wage is:

def wagePerMonth():
    print("What is your Monthly wage?")
    global wage_month
    wage_month = float(input("> ")) 
    return wage_month

# Function to get input from the user on what their yearly wage is:

def wagePerYear():
    print("What is your Annual wage?")
    global wage_year
    wage_year = float(input("> "))
    return wage_year

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


# Function to calculate wage in Hourly Format:

def calculateWageHourly():
    if dollar_pounds == "p":
        wage_per_week = wage_hour * 7
        wage_per_month = wage_per_week * 4
        wage_per_year = wage_per_month * 12

        wage_list = [
            f"Your Hourly Wage: £{wage_hour:.2f} Hourly",
            f"Your Weekly Wage: £{wage_per_week:.2f} Weekly",
            f"Your Monthly Wage: £{wage_per_month:.2f} Monthly",
            f"Your Annual Wage: £{wage_per_year:.2f} Annually",
        ]

    elif dollar_pounds == "d":
        wage_per_week = wage_hour * 7
        wage_per_month = wage_per_week * 4
        wage_per_year = wage_per_month * 12

        wage_list = [
            f"Your Hourly Wage: ${wage_hour:.2f} Hourly",
            f"Your Weekly Wage: ${wage_per_week:.2f} Weekly",
            f"Your Monthly Wage: ${wage_per_month:.2f} Monthly",
            f"Your Annual Wage: ${wage_per_year:.2f} Annually",
        ]

    printBox(wage_list)

# Function to calculate wage in Weekly Format:    
    
def calculateWageWeekly():
    if dollar_pounds == "p":
        wage_per_week = wage_week
        wage_per_hour = wage_per_week / 40
        wage_per_month = wage_per_week * 4
        wage_per_year = wage_per_month * 12

        wage_list = [
            f"Your Hourly Wage: £{wage_per_week:.2f} Weekly",
            f"Your Weekly Wage: £{wage_per_hour:.2f} Hourly",
            f"Your Monthly Wage: £{wage_per_month:.2f} Monthly",
            f"Your Annual Wage: £{wage_per_year:.2f} Annually",
        ]

    elif dollar_pounds == "d":
        wage_per_week = wage_week
        wage_per_hour = wage_per_week / 40
        wage_per_month = wage_per_week * 4
        wage_per_year = wage_per_month * 12

        wage_list = [
            f"Your Hourly Wage: ${wage_per_week:.2f} Weekly",
            f"Your Weekly Wage: ${wage_per_hour:.2f} Hourly",
            f"Your Monthly Wage: ${wage_per_month:.2f} Monthly",
            f"Your Annual Wage: ${wage_per_year:.2f} Annually",
        ]

    printBox(wage_list)

# Function to calculate wage in Monthly Format:

def calculateWageMonthly():
    if dollar_pounds == "p":
        wage_per_month = wage_month
        wage_per_week = wage_per_month / 4
        wage_per_hour = wage_per_week / 40
        wage_per_year = wage_per_month * 12

        wage_list = [
            f"Your Hourly Wage: £{wage_per_month:.2f} Monthly",
            f"Your Weekly Wage: £{wage_per_week:.2f} Weekly",
            f"Your Monthly Wage: £{wage_per_hour:.2f} Hourly",
            f"Your Annual Wage: £{wage_per_year:.2f} Annually",
        ]

    elif dollar_pounds == "d":
        wage_per_month = wage_month
        wage_per_week = wage_per_month / 4
        wage_per_hour = wage_per_week / 40
        wage_per_year = wage_per_month * 12

        wage_list = [
            f"Your Hourly Wage: ${wage_per_month:.2f} Monthly",
            f"Your Weekly Wage: ${wage_per_week:.2f} Weekly",
            f"Your Monthly Wage: ${wage_per_hour:.2f} Hourly",
            f"Your Annual Wage: ${wage_per_year:.2f} Annually",
        ]

    printBox(wage_list)

# Function to calculate wage in Annual Format:

def calculateWageAnnually():
    if dollar_pounds == "p":
        wage_per_year = wage_year
        wage_per_month = wage_per_year / 12
        wage_per_week = wage_per_month / 4
        wage_per_hour = wage_per_week / 40

        wage_list = [
            f"Your Hourly Wage: £{wage_per_year:.2f} Annually",
            f"Your Weekly Wage: £{wage_per_month:.2f} Monthly",
            f"Your Monthly Wage: £{wage_per_week:.2f} Weekly",
            f"Your Annual Wage: £{wage_per_hour:.2f} Hourly",
        ]

    elif dollar_pounds == "d":
        wage_per_year = wage_year
        wage_per_month = wage_per_year / 12
        wage_per_week = wage_per_month / 4
        wage_per_hour = wage_per_week / 40

        wage_list = [
            f"Your Hourly Wage: ${wage_per_year:.2f} Annually",
            f"Your Weekly Wage: ${wage_per_month:.2f} Monthly",
            f"Your Monthly Wage: ${wage_per_week:.2f} Weekly",
            f"Your Annual Wage: ${wage_per_hour:.2f} Hourly",
        ]

    printBox(wage_list)

# if statement to determine what mode is chosen for the starting wage

if starting_wage == "h":
    dollarsOrPounds()
    wagePerHour()
    print(f"Here are your results, {name}")
    calculateWageHourly()
    
    
elif starting_wage == "w":
    dollarsOrPounds()
    wagePerWeek()
    print(f"Here are your results, {name}")
    calculateWageWeekly()
    
    
elif starting_wage == "m":
    dollarsOrPounds()
    wagePerMonth()
    print(f"Here are your results, {name}")
    calculateWageMonthly()
    
elif starting_wage == "a":
    dollarsOrPounds()
    wagePerYear()
    print(f"Here are your results, {name}")
    calculateWageAnnually()
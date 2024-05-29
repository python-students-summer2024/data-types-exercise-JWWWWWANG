"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
    sale = float(input("what is your total sale?"))
    profit = float(sale)*0.23
    string_profit = "${:,.2f}".format(profit)
    string_sale = "${:,.2f}".format(sale)
    print("Profit:" + string_profit + "for sales of " + string_sale)


def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    number_1 = int(input("enter the first number:"))
    number_2 = int(input("enter the second number:"))
    quotient = format(number_1 / number_2)
    remainder = format(number_1 % number_2)
    print(format(number_2) + " goes into " + format(number_1) + " a total of " + quotient + " with a remainder of " + remainder)


def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """
    miles_driven = float(input("Miles driven:"))
    gas_used = float(input("Gas used:"))
    mpg = miles_driven / gas_used
    print("Miles per gallon: " + format(mpg))


def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    p1 = float(input("Enter price #1: "))
    p2 = float(input("Enter price #2: "))
    p3 = float(input("Enter price #3: "))
    string_p1 = "{:,.2f}".format(p1)
    string_p2 = "{:,.2f}".format(p2)
    string_p3 = "{:,.2f}".format(p3)
    f_p1 = format(string_p1, '>10s')
    f_p2 = format(string_p2, '>10s')
    f_p3 = format(string_p3, '>10s')
    print("\nHere are your prices!\n")
    print("Price #1: $" + f_p1)
    print("Price #2: $" + f_p2)
    print("Price #3: $" + f_p3)

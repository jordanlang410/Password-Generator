""" This program allows the user to select between 6 different functions.
The program can Generate Secure Password, Calculate and Format a Percentage,
Calculate the Days from today until July 4, 2025, Calculate the leg of a triangle,
Calculate the volume of a Right Circular Cylinder, and exit the program."""
import datetime
import math
import secrets
import string
from datetime import date

print("***********************************************************")


# Meun Options
def menu():
    """Function to print out the user menu"""
    print("Please enter a number, 1 through 6.")
    print("1: Generate Secure Password ")
    print("2: Calculate and Format a Percentage")
    print("3: Days from today until July 4, 2025?")
    print("4: Calculate the leg of a triangle")
    print("5: Calculate the volume of a Right Circular Cylinder")
    print("6: Exit program")


def gen_password(pass_length, lowercase, uppercase, numbers, special_char):
    """Function to create a random password"""
    pass_characters = lowercase + uppercase + numbers + special_char

    password = ''.join(secrets.choice(pass_characters) for i in range(pass_length))
    return password


def password_info():
    """Function to print a random password and take the the users input on:
    How long the password should be
    If they would like to include lowercase letters
    If they would like to include uppercase letters
    If they would like to include numbers
    And if they would like to include special characters"""
    pass_length = input("What would you like the length of your password to be?")
    while pass_length == "":  # ensure the user makes an entry
        pass_length = input("Your password length cannot be left blank.  Please enter an integer.")

    while not pass_length.isdigit():
        pass_length = input("Your password length must be an integer.  Please try again.")

    pass_length = int(pass_length)

    # Determine if the user would like to use Lowercase letters
    lowercase = input("Do you want to include lowercase letters"
                      " in the password? ('y' or 'n')").lower()

    while lowercase == "":  # ensure the user makes an entry
        lowercase = input("Please do not leave your entry blank.  Please enter 'y' or 'n'.").lower()

    while lowercase not in ("y", "n"):
        lowercase = input("Please only enter 'y' or 'n'.").lower()

    if lowercase == "y":
        #if the user wants lowercase letters
        use_lowercase = string.ascii_lowercase
    else:
        # leave blank if the user does not want lowercase letters
        use_lowercase = ""

    # Determine if the user would like to use Uppercase letters
    uppercase = input("Do you want to include "
                      "uppercase letters in the password? ('y' or 'n')").lower()

    while uppercase == "":  # ensure the user makes an entry
        uppercase = input("Please do not leave your entry blank.  Please enter 'y' or 'n'.").lower()

    while uppercase not in ("y", "n"):
        uppercase = input("Please only enter 'y' or 'n'.").lower()

    if uppercase == "y":
        # if the user wants uppercase letters
        use_uppercase = string.ascii_uppercase
    else:
        # leave blank if the user does not want uppercase letters
        use_uppercase = ""

    # Determine if the user would like to use Numbers
    numbers = input("Do you want to include numbers in the password? ('y' or 'n')").lower()

    while numbers == "":  # ensure the user makes an entry
        numbers = input("Please do not leave your entry blank.  Please enter 'y' or 'n'.").lower()

    while numbers not in ("y", "n"):
        numbers = input("Please only enter 'y' or 'n'.").lower()

    if numbers == "y":
        # if the user wants numbers
        use_numbers = string.digits
    else:
        # leave blank if the user does not want numbers
        use_numbers = ""

    # Determine if the user would like to use Special Characters
    special_char = input("Do you want to include special"
                         " characters in the password? ('y' or 'n')").lower()

    while special_char == "":  # ensure the user makes an entry
        special_char = input("Please do not leave "
                             "your entry blank.  Please enter 'y' or 'n'.").lower()

    while special_char not in ("y", "n"):
        special_char = input("Please only enter 'y' or 'n'.").lower()

    if special_char == "y":
        # if the user would like to use special characters
        use_special_char = string.punctuation
    else:
        # leave blank if the user does not want to use special characters
        use_special_char = ""

    # call the gen_password function and input user entries to print password
    print(gen_password(pass_length, use_lowercase, use_uppercase,
                       use_numbers, use_special_char), "\n")


def cal_percent():
    """Function to take the user input for:
    A numerator
    A denominator
    And the number of decimal places
    Then calculate the percentage based on the user entries"""

    numerator = input("Please enter a numerator.")

    while numerator == "":  # ensure the user makes an entry
        numerator = input("Please do not leave your entry blank. Please enter a numerator.")
    while True:
        #check if the numerator is an integer
        if numerator.isdigit():
            numerator = int(numerator)
            break
        # check if the numerator is a float
        if numerator.replace('.', '', 1).isdigit() and numerator.count('.') < 2:
            numerator = float(numerator)
            break
        else:
            numerator = input("Please try again. The numerator must be an number.")

    denominator = input("Please enter a denominator.")
    while denominator == "":  # ensure the user makes an entry
        denominator = input("Please do not leave your entry blank. Please enter a denominator.")
    while True:
        # check if the denominator is an integer
        if denominator.isdigit():
            denominator = int(denominator)
            break
        # check if the denominator is a float
        if denominator.replace('.', '', 1).isdigit() and denominator.count('.') < 2:
            denominator = float(denominator)
            break
        else:
            denominator = input("Please try again. The denominator must be an number.")

    decimal_place = input("Please enter the number of decimal places.")
    while decimal_place == "":  # ensure the user makes an entry
        numerator = input("Please do not leave your entry blank."
                          " Please enter the number of decimal places.")
    # ensure the user entry for decimal_place is an integer
    while not decimal_place.isdigit():
        decimal_place = input("Please try again. The decimal place must be an integer.")
    decimal_place = int(decimal_place)

    # calculate the percentage based on user entries
    percent = (numerator / denominator) * 100
    limited_float = round(percent, decimal_place)
    print(limited_float, "percent\n")


def cal_days():
    """Function to calculate the number of days from the current day until July 4th 2025"""
    today = date.today()
    future_date = datetime.date(2025, 7, 4)
    time_to_future_date = future_date - today
    print("There are", time_to_future_date.days, "days until July 4th, 2025\n")


def calc_leg_of_triangle():
    """Function to use the law of cosines to calculate the leg of a triangle"""
    a_length = input("Please enter a value for the length of side 'a'.")
    while a_length == "":  # ensure the user makes an entry
        a_length = input("Please do not leave your entry blank."
                         " Please enter a value for the length of side 'a'.")
    # ensure a_length entry is an integer
    while not a_length.isdigit():
        a_length = input("Please try again. The length of side 'a' must be an integer.")
    a_length = int(a_length)

    b_length = input("Please enter a value for the length of side 'b'.")
    while b_length == "":  # ensure the user makes an entry
        b_length = input("Please do not leave your entry blank. "
                         "Please enter a value for the length of side 'b'.")
    # ensure b_length entry is an integer
    while not b_length.isdigit():
        b_length = input("Please try again. The length of side 'b' must be an integer.")
    b_length = int(b_length)

    angle = input("Please enter a value for the angle of 'C'.")
    while angle == "":
        angle = input("Please do not leave your entry blank."
                      " Please enter a value for the angle of 'C'.")
    # ensure angle entry is an integer
    while not angle.isdigit():
        angle = input("Please try again. The angle for 'C' must be an integer.")
    angle = int(angle)

    # calculate the leg length based on user entries
    cal_cos = math.cos(math.radians(angle))
    c_length = math.sqrt(math.pow(a_length, 2) + math.pow(b_length, 2)
                         - (2 * a_length * b_length * cal_cos))
    limit_decimal_c = "{:.2f}".format(c_length)
    print("The length of side 'C' is", limit_decimal_c, "\n")


def calc_volume():
    """Function to calculate the volume of a right circular cylinder"""
    # Take user input for the radius
    radius = input("Please enter a value for the radius.")
    while radius == "":  # ensure the user makes an entry
        radius = input("Please do not leave your entry blank. Please enter a value for the radius.")

    while True:
        # check if the radius is an integer
        if radius.isdigit():
            radius = int(radius)
            break
        # check if the radius is a float
        if radius.replace('.', '', 1).isdigit() and radius.count('.') < 2:
            radius = float(radius)
            break
        else:
            radius = input("Please try again. The radius must be an number.")

    # take user input for the height
    height = input("Please enter a value for the height.")
    while height == "":  # ensure the user makes an entry
        height = input("Please do not leave your entry blank. Please enter a value for the height.")

    while True:
        # check if the height is an integer
        if height.isdigit():
            height = int(height)
            break
        # check if the height is a float
        if height.replace('.', '', 1).isdigit() and height.count('.') < 2:
            height = float(height)
            break
        else:
            height = input("Please try again. The height must be an number.")

    # Calculate the Volume based on the users entries
    volume = math.pi * (radius ** 2) * height
    limit_decimal_volume = "{:.2f}".format(volume)
    print("The volume of the cylinder is", limit_decimal_volume, "\n")


while True:
    menu()
    choice = input(">>> ")
    if choice == "1":
        password_info()

    elif choice == "2":
        cal_percent()

    elif choice == "3":
        cal_days()

    elif choice == "4":
        calc_leg_of_triangle()

    elif choice == "5":
        calc_volume()

    elif choice == "6":
        print("Thank you for using the program.")
        break
    else:
        print("Invalid choice, please choose again\n")

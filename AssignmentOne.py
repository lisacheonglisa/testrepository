"""
    Assignment Two: Temperature Conversions
    Submitted by Lisa Cheong
    Submitted: October 3, 2021

    Assignment 2: Add code to prompt the user for a temperature in Celsius and then converts that temperature to a
    specified different temperature

    Assignment 1: This program demonstrates printing lines of text to the screen
"""

def print_header():
    """Print project title and name."""
    print ("STEM Center Temperature Project")
    print ("Lisa Cheong")

def convert_units(celsius_value, units):
    """Convert celsius and return converted temperature"""
    if units == 0:
        return celsius_value
    elif units == 1:
        fahrenheit_value = celsius_value * 9/5 + 32
        return fahrenheit_value
    elif units == 2:
        kelvin_value = celsius_value + 273.15
        return kelvin_value

def main():
    print_header()
    str_temp_question = "Please enter a temperature in degrees Celsius:"
    temp_answer = float(input(str_temp_question))
    str_conv_question = "Please enter the desired conversion (0 for no conversion, 1 to convert to Fahrenheit, 2 to " \
                        "Kelvin):"
    conv_answer = int (input(str_conv_question))

    if conv_answer == 0 or conv_answer == 1 or conv_answer == 2:
        temp = convert_units(temp_answer, conv_answer)
        unit = ""
        if conv_answer == 0:
            unit = "Celsius"
        elif conv_answer == 1:
            unit = "Fahrenheit"
        elif conv_answer == 2:
            unit = "Kelvin"
        output = f"That's {temp} degrees {unit}"
        print(output)
    else:
        print ("Invalid unit entered. Please try again.")


if __name__ == "__main__":
    main()

"""
/Users/lisacheong/Desktop/Projects/CS_3A_Assignments/bin/python /Users/lisacheong/Desktop/Projects/CS_3A_Assignments/Module_2/AssignmentOne.py
STEM Center Temperature Project
Lisa Cheong
Please enter a temperature in degrees Celsius: 0
Please enter the desired conversion (0 for no conversion, 1 to convert to Fahrenheit, 2 to Kelvin): 2
That's 273.15 degrees Kelvin

Process finished with exit code 0

/Users/lisacheong/Desktop/Projects/CS_3A_Assignments/bin/python /Users/lisacheong/Desktop/Projects/CS_3A_Assignments/Module_2/AssignmentOne.py
STEM Center Temperature Project
Lisa Cheong
Please enter a temperature in degrees Celsius: 90
Please enter the desired conversion (0 for no conversion, 1 to convert to Fahrenheit, 2 to Kelvin):4
Invalid unit entered. Please try again.

Process finished with exit code 0
"""




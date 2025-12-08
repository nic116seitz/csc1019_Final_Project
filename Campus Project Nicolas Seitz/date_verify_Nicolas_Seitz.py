# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Date Verification Module
# ----------------------------------------
# Test event for debug
# test_event = "03301999" 

# This function checks if the year is a leap year 
# It first takes the year and divides it by 10000
# This will be called later in the date format function
def leap_check(event_date):
    event_year = int(event_date) % 10000
    # Then the function evaluates if the year is divisible by 100 and 400 using modulo to check if there is a remainder
    # if there is a remainder for both the year is not a leap year
    if event_year % 100 == 0 and event_year % 400 != 0:
        return False
    # If the year is divisible by 4 then the year is a leap year this function returns true
    elif event_year % 4 == 0:
        return True
    # If the year isn't divisible by 4 then the function returns false
    elif event_year % 4 != 0:
        return False
# Date format verification   
def date_format(event_date):
    # Converts the input date into a int
    try:
        # splits out the month from event date input
        month = int(event_date) % 100000000 // 1000000
        # splits out day from event date input
        day = int(event_date) % 1000000 // 10000
        # splits out the year from event date input
        format_year = int(event_date) % 10000
        # if statement to catch months with 30 days and input greater than 30 
        if (month == 3 and 
            day > 30 or month == 4 and 
            day > 30 or month == 6 and 
            day > 30 or month == 11 and 
            day > 30):
                print("Invalid Day: The month you have input only has 30 days")
                return False
        # if statement to catch if the input month has 31 days but the days input is greater then 31
        elif (month == 1 and 
              day > 31 or month == 3 and 
              day > 31 or month == 5 and 
              day > 31 or month == 7 and 
              day > 31 or month == 8 and 
              day > 31 or month == 10 and 
              day > 31 or month == 12 and 
              day > 31):
                print("Invalid Day: The month you have input only has 31 days")
                return False
        # if statement to check if the input is greater than 28 on an non leap year
        elif leap_check(event_date) == False and month == 2 and day > 28:
            print("Invalid Day: The month you have input only has 28 days")
            return False
        # if statement to check if the input is greater than 29 on a leap year
        elif leap_check(event_date) == True and month == 2 and day > 29:
            print("Invalid Day: The month you have input only has 29 days")
            return False
        # Date verification returns a true if the month and day are greater then 0 the input equals 8
        # and if the year is greater than the year 1000
        elif month > 0 and format_year > 1000 and day > 0 and len(event_date) == 8:
            return True
            # If all the previous conditions are true this will check the following and print 
            # a corresponding message:
            # input length is correct
            # month is within range
            # year is within range
        else:
            if len(event_date) != 8:
                print("Invalid date length please try again")
                return False
            elif month < 1 or month > 12:
                print("Invalid month please try again")
                return False
            elif day == 0:
                print("Invalid day please try again")
                return False
            elif format_year < 1000:
                print("Invalid year please try again")
                return False
            else:
                # Debug to catch weird errors
                print("Unexpected error (@_@)")
                return False
    # Try catch that will print a error statement prompting the user to check their input
    except ValueError:
        print("ValueError: invalid characters found in entry please check input")
        return False 

## test statement
# if date_format(test_event) == True:
#     print("Test passed!")
# else:
#     print("Failed")


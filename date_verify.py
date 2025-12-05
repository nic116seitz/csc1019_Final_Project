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
   
def date_format(event_date):
    try:
        month = int(event_date) % 100000000 // 1000000
        day = int(event_date) % 1000000 // 10000
        format_year = int(event_date) % 10000
        if (month == 3 and 
            day > 30 or month == 4 and 
            day > 30 or month == 6 and 
            day > 30 or month == 11 and 
            day > 30):
                return False
        elif (month == 1 and 
              day > 31 or month == 3 and 
              day > 31 or month == 5 and 
              day > 31 or month == 7 and 
              day > 31 or month == 8 and 
              day > 31 or month == 10 and 
              day > 31 or month == 12 and 
              day > 31):
                return False
        elif leap_check(event_date) == False and day == 2 and month > 28:
            return False
        elif month > 0 and format_year > 1000 and day > 0 and len(event_date) == 8:
            return True
        else:
            print("Unexpected Error")
            return False
    except ValueError:
        print("ValueError: invalid characters found in entry please check input")
        return False, "Value Error"
#         if len(event_date) != 8 or event_date != "1":
#              print("Invalid date length please try again")
#         elif month < 1 or month > 12:
#             print("Invalid month please try again")
#         elif day == 0:
#             print("Invalid day please try again")
#         elif format_year == 0 or format_year < 1000:
#             print("Invalid year please try again")
#         return False
 # test statement
# if date_format(test_event) == True:
#     print("Test passed!")
# else:
#     print("Failed")


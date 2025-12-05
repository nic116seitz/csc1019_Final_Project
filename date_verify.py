# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Date Verification Module
# ----------------------------------------
# test_event = "03301999" 
def leap_check(event_date):
    leap_year = int(event_date) % 10000
    if leap_year % 100 == 0 and leap_year % 400 != 0:
        return False
    elif leap_year % 4 == 0:
        return True
    elif leap_year % 4 != 0:
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


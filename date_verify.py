
# !!!!!!! DEBUG Remove Before submit !!!!!
event_date = "1202199" 
current_date = "12142025"
def past(in_date, ref_date):
    print("This is the past event function")
    pass
    
def format(in_date):
    month = int(in_date) % 100000000 // 1000000
    year = int(in_date) % 10000
    day = int(in_date) % 1000000 // 10000
    if (month > 0 and year > 1000 and day > 0 and len(in_date) == 8):
        print(in_date)
        print(f"{month}/{day}/{year}")
        return True
    else:
        if len(in_date) != 8:
            print("Invalid date length please try again")
        elif month == 0:
            print("Invalid month please try again")
        elif day == 0:
            print("Invalid day please try again")
        elif year == 0 or year < 1000:
            print("Invalid year please try again")
        return False

format(current_date)
if format(event_date) == True:
    print("Date is valid")
    past(event_date, current_date)
else:
    pass



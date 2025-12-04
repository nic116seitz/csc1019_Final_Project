# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Calendar Add Functions
# ----------------------------------------
import string
import date_verify

class Event:

    date = "1"
    location = ""
    cap = 0
    cost_per = 0.0
    tags = ""
    description_txt = "No description"
    
    def __init__(self, name):
        self.name = name
    
    def event_rev(self):
        return self.cost_per * self.capacity

    def description(self):
        return self.description_txt

events = []

def dateadd(event):
    while event.date == "1":
        verify_loop = True
        # try:
        new_event_date_raw = input("Enter the date of the event you are adding seperated by punctuation(to exit type in cancel): ")
        if new_event_date_raw.lower() == "cancel":
            return print("\nreturning to menu.....")
        else:
            date_temp = "".join(char for char in new_event_date_raw if 
                            char not in string.punctuation)
            if date_verify.date_format(date_temp) == False:
                print("The date you have selected does not exist please check date")
            else:
                event.date = date_temp                     
                verify_loop = False
                return event.date
                    # if len(event_date) != 8 or event_date != "1":
                    #     print("Invalid date length please try again")
                    # elif date_verify.month < 1 or date_verify.month > 12:
                    #     print("Invalid month please try again")
                    # elif day == 0:
                    #     print("Invalid day please try again")
                    # elif format_year == 0 or format_year < 1000:
                    #     print("Invalid year please try again")

                    
        # except AttributeError:
        #     print("AttributeError: Invalid entry please try again!!")

def addlocation(event):
    while event.location == "":
        new_event_loc_raw = input("Enter the location for your event(enter cancel to exit): ")
        # Debug Remove
        print(type(new_event_loc_raw))
        print(type(event))
        if new_event_loc_raw == "cancel":
            return print("\nreturning to menu.....")
        else:
            if len(new_event_loc_raw) == 1:
                event.location = new_event_loc_raw.upper()
            else:
                new_event_low = new_event_loc_raw.lower()
                new_event1 = new_event_low[0].upper()
                new_event2 = new_event_loc_raw[:-1]
                event.location = new_event1 + new_event2 
                # Debug Remove
                print(event.location)

def addcap(event):
    while event.cap == 0:
        new_event_cap_raw = input("Please enter the capacity of your location (type cancel to exit): ")
        if new_event_cap_raw == "cancel":
            return print("\nreturning to menu.....")
        else:
            try:
                event.cap = int(new_event_cap_raw)
            except ValueError:
                print("Invalid input please try again")

def addprice(event):
    while event.cost_per == 0.0:
        try:
            new_event_price_raw = input("Enter the cost per person for your event(type any letters to exit): ")
            if new_event_price_raw == "cancel":
                return print("\nReturning to menu >>>>>>")
            else:
                event.cost_per = float(new_event_price_raw)
        except ValueError:
            print("The number you have entered is invalid please try again")

def addtags(event):
    event.tags = "".join(char for char in input("Enter tags seperated by punctuation: ") if 
        char not in string.punctuation)

def createnew(event_list):
    new_event_name = ""
    while new_event_name == "":
        new_event_raw = input("Enter the name for your event(type in cancel to exit): ").lower()
        if new_event_raw.lower() == "cancel":
            print("\nreturning to menu.....")
            break
        elif new_event_raw in event_list:
            print("The name of the event already exists in your calendar")
        else:
            new_event_name = new_event_raw
            new_event = Event(new_event_name)
            print(new_event.name)
            dateadd(new_event)
            addlocation(new_event)
            addcap(new_event)
            addprice(new_event)
            addscript(new_event)
            addtags(new_event)
            event_list.append(new_event)
 
createnew(events)

# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Calendar Add Functions
# ----------------------------------------
# Imports for the caladd which are string for punctuation verification
import string
# date_verify for date verification
import date_verify
import cal

# Class definition for Event
class Event:
    # Each event object must have date, location, cap, cost_per, tags, and description text
    date = "1"
    location = ""
    cap = 0
    cost_per = 0.0
    tags = ""
    description_txt = "No description"
    
    def __init__(self, name):
        self.name = name
    
    def event_rev(self):
        return self.cost_per * self.cap

    def description(self):
        return self.description_txt

# Test_array for debugging caladd module
test = []

def dateadd(event):
    while event.date == "1":
        verify_loop = True
        # try:
        new_event_date_raw = input("Enter the date of the event you are adding seperated by punctuation"+
            "(to cancel type in cancel): ")
        if new_event_date_raw.lower() == "cancel":
            return print("\nreturning to menu.....")
        else:
            date_temp = "".join(char for char in new_event_date_raw if 
                            char not in string.punctuation)
            if date_verify.date_format(date_temp) == False:
                print("The date you have selected does not exist please check date or the format for your date is wrong.")
            else:
                event.date = date_temp                     
                verify_loop = False
                return event.date
        # except ValueError:
        #     print("AttributeError: Invalid entry please try again!!")

def addlocation(event):
    while event.location == "":
        new_event_loc_raw = input("Enter the location for your event(enter cancel to exit): ")
        if new_event_loc_raw == "cancel":
            return print("\nreturning to menu.....")
        else:
            if len(new_event_loc_raw) == 1:
                event.location = new_event_loc_raw.upper()
            else:
                new_event_low = new_event_loc_raw.lower()
                new_event1 = new_event_low[0].upper()
                new_event2 = new_event_loc_raw[1:]
                event.location = new_event1 + new_event2 

def addcap(event):
    while event.cap == 0:
        new_event_cap_raw = input("Please enter the capacity of your location (type cancel to exit): ")
        if new_event_cap_raw == "cancel":
            return print("\nreturning to menu.....")
        else:
            try:
                event.cap = int(new_event_cap_raw)
                if event.cap < 0:
                    event.cap = 0
            except ValueError:
                print("Invalid input please try again")

def addprice(event):
    while event.cost_per == 0.0:
        try:
            new_event_price_raw = input("Enter the cost per person for your event(type any letters to exit): ")
            if new_event_price_raw == "cancel":
                return print("\nReturning to menu >>>>>>")
            elif new_event_price raw < 0:
                event.cost_per = 0
            else:
                event.cost_per = float(new_event_price_raw)
        except ValueError:
            print("The number you have entered is invalid please try again")

def addtags(event):
    event.tags = ",".join(char.strip() for char in input("Enter tags seperated by punctuation: ") if 
        char not in string.punctuation)

def addscript(event):
    event.description_txt = input("Enter a description for your Event: ")

def createnew(event_list):
    new_event_name = ""
    while new_event_name == "":
        new_event_raw = input("Enter the name for your event(type in cancel to exit): ").lower()
        if new_event_raw == "cancel":
            print("\nreturning to menu.....")
            break
        elif new_event_raw in event_list:
            print("The name of the event already exists in your calendar")
        else:
            new_event_name1 = new_event_raw[0].upper()
            new_event_name2 = new_event_raw[1:].lower()
            new_event_name = new_event_name1 + new_event_name2
            new_event = Event(new_event_name)
            dateadd(new_event)
            addlocation(new_event)
            addcap(new_event)
            addprice(new_event)
            addscript(new_event)
            addtags(new_event)
            event_list.append(new_event)

# Test function call and print for debugging the caladd module 
createnew(test)
test_event = test[0]
print("New Event Created!")
print("*******\n")
print(f"Name: {test_event.name}")
print(f"Location: {test_event.location}")
print(f"Date: {test_event.date}")
print(f"Capacity: {test_event.cap}")
print(f"Cost per person: {test_event.cost_per}")
print(f"Tags: {test_event.tags}")
print(f"Description: {test_event.description()}")
print(f"Projected Revenue: {test_event.event_rev()}")
print("*******")



# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Calendar Add Functions
# ----------------------------------------
# Class definition for event objects
import string
from date_verify import *
class Event:
    # Each event object must have date, location, cap, cost_per, tags, and description text
    # Negative values were selected as the 
    date = ""
    location = ""
    cap = 0
    cost_per = 0
    tags = []
    description_txt = "No description"
    # This is the __init__ for the class Event objects
    def __init__(self, name):
        self.name = name
    # This is the event_rev method which returns the cost of the event, multiplied by the capcity of the event
    def event_rev(self):
        return self.cost_per * self.cap

    # This is the description method which returns the description attribute of the class: Event
    def description(self):
        return self.description_txt

# Test_array for debugging caladd module
# test = []

# This is the function that adds date to the event 
def dateadd(event):
    date_loop = True
    while date_loop == True:
        # the function will prompt the user for the input date that will be assigned to the var
        # new_event_date_raw
        new_event_date_raw = input("Enter the date of the event you are adding seperated by punctuation"+
            "(to cancel type in cancel): ")
        # If the new_event_date_raw converted into lowercase == cancel then the function will break
        # printing the message that the user will be going back to the main menu
        if new_event_date_raw.lower() == "cancel":
            date_loop = False
            return print("\nreturning to menu.....")
        # If the new date is not cancel
        # Then the function will enter its final evaluation 
        else:
            # The function takes the raw date and removes the punctuation turning it into a string of num
            date_temp = "".join(char for char in new_event_date_raw if 
                            char not in string.punctuation)
            # This looks for the False bool in the return statement of the date_temp if it returns false it prints the error message below
            if date_format(date_temp) == False:
                print("Invalid date")
            # If the date_temp passes all the previous checks then the event is overwritten thus breking the loop
            # Another way to do this would be to use False as the place holder value event.date
            else:
                event.date = date_temp                     
                date_loop = False
                return event.date

# This is the function that adds the location to the event
def addlocation(event):
    location_loop = True
    # If the attribute event.location is empty the loop will trigger
    while location_loop == True:
        # The function then prompts the user to input the location for the event
        # if it is equal to cancel then the function will print the returning to menu statement
        # otherwise it will process the string by converting it to upper case if the length of the event name is 1
        new_event_loc_raw = input("Enter the location for your event(enter cancel to exit): ").lower()
        if new_event_loc_raw == "cancel":
            location_loop = False
            return print("\nreturning to menu.....")
        else:
            # If the length of the event name is 1 then that letter is converted to uppercase
            if len(new_event_loc_raw) == 1:
                event.location = new_event_loc_raw.upper()
            # If the user inputs a blank statement then it prints an error and goes to the top of the loop
            elif new_event_loc_raw.strip() == "":
                print("Error: no location entered")
            # If the input for location passes all previous checks then the location is formatted using string slicing of the first index
            # and then slicing of the rest of the word minus the first character with the lower function
            # the result is then bound to the attribute location
            else:
                new_event_low = new_event_loc_raw.lower()
                new_event1 = new_event_low[0].upper()
                new_event2 = new_event_loc_raw[1:]
                event.location = new_event1 + new_event2 
                location_loop = False
# This the function that adds capacity to a given object
def addcap(event):
    # Loop condition var 
    cap_loop = True
    # Loop checks condition var to see if it should loop
    while cap_loop == True:
        try:
            # The function prompts the user for their input for the capacity and stores it to the var new_event_cap_raw
            # if this variable == cancel then the user will be taken back to the main menu
            new_event_cap_raw = input("Please enter the capacity of your location (type cancel to exit): ")
            if new_event_cap_raw == "cancel":
                cap_loop = False
                return print("\nreturning to menu.....")
            # otherwise the function will bind the capacity to the attribute cap 
            # if the capacity triggers a ValueError (in the case of being non int) it will print invalid input and reset the loop
            # if the capacity is less then 0 then it will be rebound to 0
            # condition var (for the loop) is then set to False
            else:
                if int(new_event_cap_raw) < 0:
                    print("Invalid Capacity: Event capacity cannot be less then 0")
                else: 
                    event.cap == int(new_event_cap_raw)
                    cap_loop = False
        except ValueError:
            print("Invalid Input: please use whole numbers to describe capacity")

# This is the function that adds price to a given event
def addprice(event):
    # Loop condition var
    price_loop = True
    # loop will check condition var to see if it should loop
    while price_loop == True:
        # Try except to see if there is a ValueError (in the case of non number entries)
        try:
            # prompts user to but in their desired event price
            # if they input cancel then they are sent to the main menu
            new_event_price_raw = input("Enter the cost per person for your event(type any letters to exit): ").lower()
            if new_event_price_raw == "cancel":
                price_loop = False
                return print("\nReturning to menu >>>>>>")
            # If the user tries to enter a negative number the error mesage prints sending them back to the top of the loop
            elif int(new_event_price_raw) < 0:
                print("Invalid Price: Event price cannot be less then 0")
            # If the event price passes all previous checks then the input is bound to to the attribute cost_per 
            else:
                event.cost_per = float(new_event_price_raw)
                price_loop = False
        except ValueError:
            print("The number you have entered is invalid please try again")

# Takes input and converts it to tags for the given event
def addtags(event):
    add_tags_loop = True
    while add_tags_loop == True:
        event_tags_raw = input("Enter the tags seperated by commas(cancel to exit): ").lower()
        if event_tags_raw == "cancel":
            return print("\nreturning to menu.....")
        elif "," not in event_tags_raw:
            add_tags_loop = False
            event.tags = event_tags_raw
        elif event_tags_raw == "":
            break
        else:
            # This part checks over to see if the punctuation is not , if  it is it will throw an error 
            for ch in string.punctuation:
                if ch in event_tags_raw and ch != ",":
                    print("Invalid punctuation detected")
                else:
                    add_tags_loop = False
                    event.tags = event_tags_raw.split(",")
    
# Add description function
# prompts the user for input for their desired description text then binds it to the object attribute description_txt
def addscript(event):
    event.description_txt = input("Enter a description for your Event: ")

# This is the create new function
def createnew(event_list):
    # Loop condition var
    create_loop = True
    # Loop checks condition
    while create_loop == True:
        # prompts user to input which it converts to lowercase
        new_event_raw = input("Enter the name for your event(type in cancel to exit): ").lower()
        # If the user inputs cancel in any case it will terminate the loop exiting to the main menu
        if new_event_raw == "cancel":
            create_loop = False
            return ("\nreturning to menu.....")
        # Checks for duplicate events
        elif new_event_raw in event_list:
            print("The name of the event already exists in your calendar")
        # Otherwise it will format the input name and create a new instance of the object with the input name
        # it then calls the other functions in order to reassign the attributes for the event
        # it then takes the input event_list array and appends it with the event
        else:
            # the new_event_name vars are used to create a name that has the first letter capitalized while the other letters remain un capitalized
            new_event_name1 = new_event_raw[0].upper()
            new_event_name2 = new_event_raw[1:].lower()
            new_event_name = new_event_name1 + new_event_name2
            new_event = Event(new_event_name)
            # This calls the other functions to edit the attributes of the event
            dateadd(new_event)
            addlocation(new_event)
            addcap(new_event)
            addprice(new_event)
            addscript(new_event)
            addtags(new_event)
            event_list.append(new_event)
            # These print the various attributes for the event
            print("New Event Created!")
            print("*******\n")
            print(f"Name: {new_event.name}")
            print(f"Location: {new_event.location}")
            print(f"Date: {new_event.date}")
            print(f"Capacity: {new_event.cap}")
            print(f"Cost per person: {new_event.cost_per}")
            print(f"Tags: {new_event.tags}")
            # Thse call the class methods
            print(f"Description: {new_event.description()}")
            print(f"Projected Revenue: {new_event.event_rev()}")
            print("*******")
            create_loop = False

# Test function call and print for debugging the caladd module 
# createnew(test)
# test_event = test[0]
# print("New Event Created!")
# print("*******\n")
# print(f"Name: {test_event.name}")
# print(f"Location: {test_event.location}")
# print(f"Date: {test_event.date}")
# print(f"Capacity: {test_event.cap}")
# print(f"Cost per person: {test_event.cost_per}")
# print(f"Tags: {test_event.tags}")
# print(f"Description: {test_event.description()}")
# print(f"Projected Revenue: {test_event.event_rev()}")
# print("*******")



# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Calendar Module
# ----------------------------------------
import string
import main
# import date_verify
class Event:

    date = ""
    location = ""
    capacity = 0
    cost_per = 0.0
    tags = ""
    description_txt = "No description"
    
    def __init__(self, name):
        self.name = name
    
    def event_rev(self):
        return self.cost_per * self.capacity

    def description(self):
        print(self.description_txt)

events = main.events

def createnew(event_list):
    new_event_name = ""
    while new_event_name == "":
        new_event_raw = input("Enter the name for your event(type in cancel to exit): ")
        if new_event_raw.lower() == "cancel":
            print("\nreturning to menu.....")
            break
        elif new_event_raw in event_list:
            print("The name of the event already exists in your calendar")
        else:
            new_event_name = new_event_raw
            new_event = Event(new_event_name)
            dateadd(new_event)
            addlocation(new_event)
            addcap(new_event)
            addprice(new_event)
            addscript(new_event)
            addtags(new_event)
            event_list.append(new_event)
            
def dateadd(event):
    while event.date == "":
        try:
            new_event_date_raw = input("Enter the date of the event you are adding seperated by punctuation(to exit type in cancel): ")
            if new_event_date_raw.lower() == "cancel":
                return print("\nreturning to menu.....")
            else:
                # Loop in the date verification here
                event.date = "".join(char for char in new_event_date_raw if 
                    char not in string.punctuation)
                return event.date
        except AttributeError:
            print("Invalid entry please try again!!")

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
                new_event1 = new_event_loc_raw.split(0)
                new_event2 = new_event_loc_raw.split(-(len(new_event_loc_raw) - 1))
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

def remove(events_list, search_name):
    for event in events_list:
        if event.name == search_name:
            events_list.remove(search_name)
        else:
            print("Event not found please try again!!")

def addtags(event):
    event.tags = "".join(char for char in input("Enter tags seperated by punctuation: ") if 
        char not in string.punctuation)

def edit(events_list):
    edit_loop = True
    while edit_loop == True:
        edit_target = (input("\nPlease select the event you would like to edit")).lower()
        if edit_target in events_list:
            edit_loop = False
        else:
            print("Invalid entry please try again!")

    field_loop == True
    while field_loop == True:
        try:
            field_target = int(input("\nPlease select the field of the event you would" + 
                "like to edit from the list\n"+
                "1) Name\n" +
                "2) Date\n" +
                "3) Location\n" +
                "4) Tags\n" +
                "5) Description\n" +
                "6) Quit"))
            if field_target == 1:
                edit_target_rename == (input("Enter the new name you would like to put for the event: ")).lower()
                if edit_target_rename == "cancel":
                    pass
                else: 
                    edit_target.name = edit_target_rename
                    field_loop = False
            elif field_target == 2:
                dateadd(edit_target)
                field_loop = False
            elif field_target == 3:
                addlocation(edit_target)
                field_loop = False
            elif field_target == 2:
                addtags(edit_target)
                field_loop = False
            elif field_target == 3:
                addscript(edit_target)
                field_loop = False
            elif field_target == 2:
                print("\n Returning to menu....")
                field_loop = False
        except ValueError:
            print("Your entry was non numerical please try again")

def addscript(event):
    event_script = input("Enter in a short description for event"+
        "\n(enter cancel if you would like to exit):")

def listall(event_list):
    for event in enumerate(events, start=1):
        print("*******\n")
        print(f"Name: {event.name}")
        print(f"Date: {event.date}")
        print(f"Cost per person: {event.cost_per}")
        print(f"Date: {event.capacity}")
        print(f"Date: {event.location}")
        print(f"")
        print("*******")
             
created_event = createnew(events)
event_date = dateadd(created_event)
addlocation(created_event)
addcap(created_event)
addprice(created_event)

# Debugs put using method calls put this in the main program

print()


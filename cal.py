# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Calendar Module
# ----------------------------------------
# The calendar module has the following imports string, to call string.punctuation
import string
import date_verify
# This is the remove event function
def remove(events_list, targ_name):
    # This iterates over each of the events in the given events_list
    for event in events_list:
        if targ_name in event.name:
            print("")
            print(event.name)
            events_list.remove(targ_name)
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
                cal.addscript(edit_target)
                field_loop = False
            elif field_target == 2:
                print("\n Returning to menu....")
                field_loop = False
                # Possible failcheck functionality that I have to figure out a way to loop in
                    # if len(event_date) != 8 or event_date != "1":
                    #     print("Invalid date length please try again")
                    # elif date_verify.month < 1 or date_verify.month > 12:
                    #     print("Invalid month please try again")
                    # elif day == 0:
                    #     print("Invalid day please try again")
                    # elif format_year == 0 or format_year < 1000:
                    #     print("Invalid year please try again")
        except ValueError:
            print("Your entry was non numerical please try again")

def listall(event_list):
    if events_list == []:
        print("You currently have no events in your calendar")
    else:
        for event in enumerate(event_list, start=1):
           print(event) 

def search(event_list):
    print("This is the search method of the cal module ... ")
    pass

# Given extra time format these strings
def print(event):                 
    print("New Event Created!")
    print("*******\n")
    print(f"Name: {event.caladd.date}")
    print(f"Date: {event.caladd.location}")
    print(f"Capacity: {event.caladd.cap}")
    print(f"Cost per person: {event.caladd.cost_per}")
    print(f"Tags: {event.caladd.tags}")
    print(f"Description: {event.caladd.description()}")
    print(f"Description: {event.caladd.event_rev()}")
    print("*******")


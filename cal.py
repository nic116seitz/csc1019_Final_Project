# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Calendar Module
# ----------------------------------------
import string
import main

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
                cal.addcript(edit_target)
                field_loop = False
            elif field_target == 2:
                print("\n Returning to menu....")
                field_loop = False
        except ValueError:
            print("Your entry was non numerical please try again")


def listall(event_list):
    if events_list == []:
        print("You currently have no events in your calendar")
    else:
        for event in enumerate(event_list, start=1):
            print("*******\n")
            print(f"Name: {event.name}")
            print(f"Date: {event.date}")
            print(f"Cost per person: {event.cost_per}")
            print(f"Date: {event.capacity}")
            print(f"Date: {event.location}")
            print(f"")
            print("*******")
                 



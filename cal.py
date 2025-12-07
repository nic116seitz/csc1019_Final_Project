# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Calendar Module
# ----------------------------------------
from caladd import *
from stats import *
events = []
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
            elif field_target == 4:
                addtags(edit_target)
                field_loop = False
            elif field_target == 5:
                addscript(edit_target)
                field_loop = False
            elif field_target == 6:
                print("\n Returning to menu....")
                menu_loop = False
        except ValueError:
            print("Your entry was non numerical please try again")

def listall(event_list):
    if events_list == []:
        print("You currently have no events in your calendar")
    else:
        for event in enumerate(event_list, start=1):
            eventprint(event)
            
def search(event_list, query):
    event_names = []
    for event in event_list:
        if query in event.name or query in event:
            event_names += event 
            print(event_names)
    for event in event_names:
        if event_name in enumerate(event_list, start= 1):
            eventprint(event)
        
def eventprint(event):
    print("*******\n")
    print(f"Name: {event.name}")
    print(f"Date: {event.date}")
    print(f"Date: {event.location}")
    print(f"Capacity: {event.cap}")
    print(f"Cost per person: {event.cost_per}")
    print(f"Tags: {event.tags}")
    print(f"Description: {event.description_txt}")
    print(f"Projected revenue: {event.event_rev()}")
    print("*******")

# Caller function to print stats
def printstats(event_list):
    print(f"most expensive: {mostexpensive(event_list)}")
    print(f"cheapest: {cheapest(event_list)}")
    print(f"average rev: {averagerev(event_list):.2f}")
    print(f"least rev: {leastrev(event_list):.2f}")
    print(f"highest rev: {highestrev(event_list):.2f}")
# This is the menu function
def menu(events_list):
    # Loop condition var
    menu_loop = True
    # While loop to show the main menu,
    # an alt method to do this would be to construct an array of options and then enumerate said array
    # then create a for loop that will print the array
    while menu_loop == True:
        print("*******************\n",
              "Main Menu\n",
              "*******************\n",
              "1) Add New Event\n",
              "2) View all Events\n",
              "3) Search For Events\n",
              "4) Remove Events\n",
              "5) Event Calendar Summary\n",
              "6) Quit")
        # Prompts user to make a selection from the given menu
        usr_choice = input(" Enter Menu Selection: ")
        # Triggers the create new event function see caladd module (line 174)
        if usr_choice == "1":
            new_event = createnew(events)
            eventprint(new_event)
        elif usr_choice == "2":
            listall(events)
        elif usr_choice == "3":
            print("This is the search events function")
        elif usr_choice == "4":
            remove(events)
        elif usr_choice == "5":
            printstats(events_list)
        elif usr_choice == "6":
            print("Goodbye :)")
            menu_loop = False
        else:
            print("Invalid input! Please, try again!")
menu(events)



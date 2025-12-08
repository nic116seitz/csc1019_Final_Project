# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Calendar Add Functions
# ----------------------------------------
# Class definition for event objects
import random
import string
from date_verify import *

events = []
# Class definition for class event
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

# Test_array for debugging caladd section
# test = []

# This is the function that adds date to the event 
def date_add(event):
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
            # This looks for the False bool in the return statement of the date_temp if it returns false it allows date_verify 
            # print the error message
            if date_format(date_temp) == False:
                pass
            # If the date_temp passes all the previous checks then the event is overwritten thus breking the loop
            # Another way to do this would be to use False as the place holder value event.date
            else:
                event.date = date_temp                     
                date_loop = False
                return event.date

# This is the function that adds the location to the event
def add_location(event):
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
def add_cap(event):
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
                    event.cap = int(new_event_cap_raw)
                    cap_loop = False
        except ValueError:
            print("Invalid Input: please use whole numbers to describe capacity")

# This is the function that adds price to a given event
def add_price(event):
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
def add_tags(event):
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
def add_script(event):
    event.description_txt = input("Enter a description for your Event: ")

# This is the create new function
def create_new(event_list):
    # Loop condition var
    create_loop = True
    # Loop checks condition
    while create_loop == True:
        # prompts user to input which it converts to lowercase
        new_event_raw = input("Enter the name for your event(type in cancel to exit): ").lower()
        # If the user inputs cancel in any case it will terminate the loop exiting to the main menu
        if new_event_raw == "cancel":
            create_loop = False
            return "\nreturning to menu....."
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
            date_add(new_event)
            add_location(new_event)
            add_cap(new_event)
            add_price(new_event)
            add_script(new_event)
            add_tags(new_event)
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

# ----------------------------------------
# Campus Event Planner: Calendar Functions
# ----------------------------------------
# This is the remove event function
def remove(events_list, targ_name):
    # This iterates over each of the events in the given events_list
    for event in events_list:
        if targ_name in event.name:
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
    field_loop = True
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
                edit_target_rename = (input("Enter the new name you would like to put for the event: ")).lower()
                if edit_target_rename == "cancel":
                   pass
                else: 
                    field_target.name = edit_target_rename
                    field_loop = False
            elif field_target == 2:
                date_add(event_list)
                field_loop = False
            elif field_target == 3:
                add_location(event_list)
                field_loop = False
            elif field_target == 4:
                add_tags(event_list)
                field_loop = False
            elif field_target == 5:
                add_script(event_list)
                field_loop = False
            elif field_target == 6:
                print("\n Returning to menu....")
                menu_loop = False
        except ValueError:
            print("Your entry was non numerical please try again")
# prints all events in the event list and numbers them
def listall(event_list):
    if event_list == []:
        print("You currently have no events in your calendar")
    else:
        for event in event_list:
            eventprint(event)
            
def search(event_list, query):
    match = []
    query = (query.lower()).split(" ")
    for event in event_list:
        for word in query:
            word_cap = word[0].upper() + word[1:]
            if word in event.name or word_cap in event.name:
                match.append(event)
    if match == []:
        print("No match Found!")
    else:
        for event_match in match:
            eventprint(event_match)

# function to print event info on a per event basis        
def eventprint(event):
    print("*******\n")
    print(f"Name: {event.name}")
    print(f"Date: {event.date}")
    print(f"Date: {event.location}")
    print(f"Capacity: {event.cap}")
    print(f"Cost per person: {event.cost_per}")
    print(f"Tags: {event.tags}")
    print(f"Description: {event.description_txt}")
    print(f"Projected revenue: {event.cost_per * event.cap}")
    print("*******")

# This is a test function that generates 3 random events in order to test that the statistics functions work
event_inc = 1
print("Debug at line 310")
for num in range(4):
    ran_event = Event("event0")
    ran_event.cap = random.randint(1, 12)
    ran_event.cost_per = random.randint(10, 1000) / 10
    ran_event.description_txt = f"Random {event_inc}"
    ran_event.tags = ["random"]
    ran_event.location = "Random"
    # print("Name:", ran_event.name)
    # print("Cap:", ran_event.cap)
    # print("cost_per:", ran_event.cost_per)
    # print("event_descript:", ran_event.description_txt)
    # print("event_rev:", ran_event.event_rev())
    event_inc += 1
    events.append(ran_event)

# Function finds the most expensive event
# This then returns the name of whatever event wins this comparison
def mostexpensive(events_list):
    most_exp = Event("Empty")
    for event in events_list:
        if event.cost_per > most_exp.cost_per:
            most_exp = event
    return [most_exp.name, most_exp.cost_per]
# This does the same as the previous function but looks for the lowest cost_per and returns the name of that with cost_per
def cheapest(events_list):
    cheapest = Event("Empty")
    cheapest.cost_per = float('inf')
    for event in events_list:
        if event.cost_per < cheapest.cost_per:
            cheapest = event
    return [cheapest.name, cheapest.cost_per]
# This function generates a list of costs_per and then calculates the average by calculating the sum of said list and dividing
# it by the length (of said list)
def averageprice(events_list):
    list_avg_price = []
    for event in events_list:
        list_avg_price.append(event.cost_per)
    average_price = sum(list_avg_price) / len(list_avg_price)  
    return average_price
# This generates the average revenue of all events by adding the revenue of each event to a list and then dividing it by the length of said list
# note: one of the issues with the built in method was its inaccessibility in for loops I would love to know how to apply iter here but failed to understand
# how to apply it in this context
def averagerev(events_list):
    list_rev_avg = []
    for event in events_list:
        list_rev_avg.append(event.cap * event.cost_per)
    average_rev = sum(list_rev_avg) / len(list_rev_avg)  
    return average_rev
# This compares the revenue of all events and spits out the lowest revenue for all the events in the event list
def leastrev(events_list):
    least = Event("Empty")
    least_rev = float('inf')
    for event in events_list:
        current_least_rev = event.cost_per * event.cap
        if current_least_rev < least_rev:
            least_rev = current_least_rev
    return  least_rev

# This compare the revenue of all evnts and spits out the highest revenue for all the events in the event list
def highestrev(events_list):
    highest = Event("Empty")
    highest_rev = highest.cost_per * highest.cap
    for event in events_list:
        current_highest_rev = event.cost_per * event.cap
        if current_highest_rev > highest_rev:
            highest_rev = current_highest_rev
    return highest_rev

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
            new_event = create_new(events)
        elif usr_choice == "2":
            listall(events)
        elif usr_choice == "3":
            search(events, input("Enter search query: "))
        elif usr_choice == "4":
            remove(events, input("Enter the name of the event you would like to remove: "))
        elif usr_choice == "5":
            printstats(events_list)
        elif usr_choice == "6":
            print("Goodbye :)")
            menu_loop = False
        else:
            print("Invalid input! Please, try again!")
menu(events)



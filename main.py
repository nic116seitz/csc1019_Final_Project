# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner
# ----------------------------------------
import string
import date_verify
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

events = []

def most_expensive(events_list):
    for event in events_list:
        current_event = events.pop(0)
        most_expensive = Event("Empty")
        if event.cost_per > most_expensive.cost_per:
            most_expensive = event
    print("The most expensive event is: ",
          event.name, "Cost:", 
          (event.cost_per * event.capacity)) # Maybe format this using fstring

def calendar_sum(events_list):
    for event in event_list:
        cal_sum = 0
        cal_sum += (event.capacity * event.cost_per)
    print(f"The total sum of all calendar events is: {cal_sum:2f}")

def cal_remove(events_list):
    print("Would you like to select event(s) by name or date?")
    target_type = input("Selection: ")
    if target_type.lower() == "name":
        target_name = input("Please enter the name of the event you would like to remove: ")
        for event in events_list.name:
            pass
        # make a list of event names => from there use that as the the input for the pop method
    elif target_type.lower() == "date":
        target_date_raw = input("Please enter the date of the event you would like to remove: ")
        target_date = "".join(char for char in target_date_raw if char not in string.punctuation)

# A function to allow users to edit each of the events on the events list
def cal_edit(events_list):
    pass

def cal_add(events_list):
    new_event_raw = input("Enter the name for your event(type in cancel to exit): ")
    if new_event_raw.lowercase() == "cancel":
        break
    else:
        new_event = Event(new_event_raw)
        new_event_date_raw = input("Enter the date of the event you are adding seperated by punctuation(to exit type in cancel): ")
        if new_event_date_raw.lowercase() == "cancel":
            break
        else:
            new_event.date = "".join(char for char in new_event_date_raw if 
                char not in string.punctuation)
            new_event_loc_raw = input("Enter the location for your event")
            if new_event_loc_raw == "cancel":
                break
            else:
                try:
                    new_event.location = (new_event_loc_raw.lowercase()).uppercase([0])
                    new_event_cap_raw = input("Please enter the capacity of your location (type cancel to exit): ")
                    if new_event_cap_raw == "cancel":
                        print("\nReturning to menu >>>>>>")
                        break
                    else:
                        new_event.cap = int(new_event_cap_raw)
                        try:
                            new_event_price = int(input("Enter the cost per person for your event(type any letters to exit): "))
                            if new_event_price_raw == "cancel":
                                print("\nReturning to menu >>>>>>")
                            else:
                                new_event_price
                        except ValueError:
                            print("The number you have entered is invalid please try again")
                except ValueError:
                    print("The number you have entered is invalid please try again")
    print(events)

def menu(events_list):
    while True:
        print("*******************\n",
              "Main Menu\n",
              "*******************\n",
              "1) Add New Event\n",
              "2) View all Events\n",
              "3) Search For Events\n",
              "4) Remove Events\n",
              "5) Event Calendar Summary\n",
              "6) Quit")
        usr_choice = input(" Enter Menu Selection: ")
        if usr_choice == "1":
            cal_add(events_list)
        elif usr_choice == "2":
            print("This is the View all events function")
            if events_list == []:
                print("You currently have no events in your calendar")
            for events_list in enumerate(events, start=1):
                print("*******\n")
                print(f"Name: {events_list.name}")
                print(f"Date: {events_list.date}")
                print(f"Cost per person: {events_list.cost_per}")
                print(f"Date: {events_list.capacity}")
                print(f"Date: {events_list.location}")
                print(f"")
                print("*******")
                
        elif usr_choice == "3":
            print("This is the search events function")
        elif usr_choice == "4":
            print("This is the remove events function")
        elif usr_choice == "5":
            cal_sum(events_list)
            print("This is the summary function")
        elif usr_choice == "6":
            print("Goodbye :)")
            exit()
        else:
            print("Invalid input! Please, try again!")

menu(events)

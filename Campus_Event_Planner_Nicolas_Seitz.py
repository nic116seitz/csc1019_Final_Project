# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner
# ----------------------------------------
import string
import month_verify
class Event:

    date = ""
    location = ""
    capacity = 0
    cost_per = 0.0
    tags = ""
    
    def __init__(self, name):
        self.name = name
    
    def event_rev(self):
        return self.cost_per * self.capacity

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
        new_event = Event(input("Enter the name for your event: "))
        new_event_date_raw = input("Enter the date of the event you are adding seperated by punctuation: ")
        new_event_date = "".join(char for char  in new_event_date_raw if char not in string.punctuation)
        events += new_event
        print(events)
    elif usr_choice == "2":
        print("This is the View all events function")
        if events == []:
            print("You currently have no events in your calendar")
        for event in enumerate(events, start=1):
            print("*******\n")
            print(f"Name: {event.name}")
            print(f"Date: {event.date}")
            print(f"Cost per person: {event.cost_per}")
            print(f"Date: {event.capacity}")
            print(f"Date: {event.location}")
            print(f"")
            print("*******")
            
    elif usr_choice == "3":
        print("This is the search events function")
    elif usr_choice == "4":
        print("This is the remove event function")
    elif usr_choice == "5":
        cal_sum(events)
        print("This is the summary function")
    elif usr_choice == "6":
        print("Goodbye :)")
        exit()
    else:
        print("Invalid input! Please, try again!")


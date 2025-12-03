import string
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

def createnew(event_list):
    new_event_raw = input("Enter the name for your event(type in cancel to exit): ")
    if new_event_raw.lower() == "cancel":
        return print("\nreturning to menu.....")
    else:
        new_event = Event(new_event_raw)
        event_list.append(new_event)
        return new_event
        
def dateadd(event):
    try:
        new_event_date_raw = input("Enter the date of the event you are adding seperated by punctuation(to exit type in cancel): ")
        if new_event_date_raw.lower() == "cancel":
            return print("\nreturning to menu.....")
        else:
            # Loop in the date verification here
            event.date = "".join(char for char in new_event_date_raw if 
                char not in string.punctuation)

    except AttributeError:
        print("Invalid entry please try again!!")

def addlocation(event):
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
    new_event_cap_raw = input("Please enter the capacity of your location (type cancel to exit): ")
    if new_event_cap_raw == "cancel":
        return print("\nreturning to menu.....")
    else:
        try:
            event.cap = int(new_event_cap_raw)
        except ValueError:
            print("Invalid input please try again")

def addprice(event):
        try:
            new_event_price_raw = input("Enter the cost per person for your event(type any letters to exit): ")
            if new_event_price_raw == "cancel":
                return print("\nReturning to menu >>>>>>")
            else:
                new_event_price = float(new_event_price_raw)
        except ValueError:
            print("The number you have entered is invalid please try again")
                
created_event = createnew(events)
dateadd(created_event)
addlocation(created_event)
addcap(created_event)
addprice(created_event)

# Debugs put using method calls put this in the main program

print(events)


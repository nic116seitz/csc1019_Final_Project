# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Statistics
# ----------------------------------------
import main
events = main.events

def mostexpensive(events_list):
    for event in events_list:
        current_event = events.pop(0)
        most_expensive = Event("Empty")
        if event.cost_per > most_expensive.cost_per:
            most_expensive = event
    print("The most expensive event is: ",
          event.name, "Cost:", 
          (event.cost_per * event.capacity)) # Maybe format this using fstring
    
def average(events_list):
    pass
 

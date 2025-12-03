# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Statistics
# ----------------------------------------
import main
events = main.events

def most_expensive(events_list):
    for event in events_list:
        current_event = events.pop(0)
        most_expensive = Event("Empty")
        if event.cost_per > most_expensive.cost_per:
            most_expensive = event
    print("The most expensive event is: ",
          event.name, "Cost:", 
          (event.cost_per * event.capacity)) # Maybe format this using fstring

    for event in event_list:
        sum = 0
        sum += (event.capacity * event.cost_per)
    print(f"The total sum of all calendar events is: {sum:2f}")
    return sum

def most_expensive(events_list):
    for event in events_list:
        current_event = events.pop(0)
        most_expensive = Event("Empty")
        if event.cost_per > most_expensive.cost_per:
            most_expensive = event
    print("The most expensive event is: ",
          event.name, "Cost:", 
          (event.cost_per * event.capacity)) # Maybe format this using fstring

def average(events_list):
 

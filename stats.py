# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Statistics Module
# ----------------------------------------
# from caladd import Event
# import random
# event_inc = 1
# test = []
# This is a test function that generates 3 random events in order to test that the statistics functions work
#   for num in range(3):
#     ran_event = Event(f"event0{event_inc}")
#     ran_event.cap = random.randint(1, 12)
#     ran_event.cost_per = random.randint(1000, 100000) / 1000000
#     print("Name:", ran_event.name)
#     print("Cap:", ran_event.cap)
#     print("cost_per:", ran_event.cost_per)
#     print("event_rev:", ran_event.event_rev())
#     event_inc += 1
#     test.append(ran_event)

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
# This compares the revenue of all events and spits out the highest revenue event for all events
def highestrev(events_list):
    highest = Event("Empty")
    highest_rev = highest.cost_per * highest.cap
    for event in events_list:
        current_highest_rev = event.cost_per * event.cap
        if current_highest_rev > highest_rev:
            highest_rev = current_highest_rev
    return highest_rev
# These are debug print statements to test that all the functions work
# print(f"most expensive: {mostexpensive(test)}")
# print(f"cheapest: {cheapest(test)}")
# print(f"average rev: {averagerev(test):.2f}")
# print(f"least rev: {leastrev(test):.2f}")
# print(f"highest rev: {highestrev(test):.2f}")

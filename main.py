# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Main
# ----------------------------------------
import calendar
import 
def most_expensive(events_list):
    for event in events_list:
        current_event = events.pop(0)
        most_expensive = Event("Empty")
        if event.cost_per > most_expensive.cost_per:
            most_expensive = event
    print("The most expensive event is: ",
          event.name, "Cost:", 
          (event.cost_per * event.capacity)) # Maybe format this using fstring


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
# This is for date verification down the line
    # if format(event_date) == True:
    #     print("Date is valid")
    #     past(event_date, current_date)
    # else:
    #     pass
menu(events)

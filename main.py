# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Main
# ----------------------------------------
import cal
import caladd

events = []

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
            test_event = caladd.createnew(events)          
            print("*******\n")
            print(f"Name: {event.caladd.date}")
            print(f"Date: {event.caladd.location}")
            print(f"Capacity: {event.caladd.cap}")
            print(f"Cost per person: {event.caladd.cost_per}")
            print(f"Tags: {event.caladd.tags}")
            print(f"Description: {event.caladd.description()}")
            print(f"Description: {event.caladd.event_rev()}")
            print("*******")
        elif usr_choice == "2":
            print("This is the View all Function")
        elif usr_choice == "3":
            print("This is the search events function")
        elif usr_choice == "4":
            print("This is the remove events function")
        elif usr_choice == "5":
            cal.cal_sum(events_list)
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

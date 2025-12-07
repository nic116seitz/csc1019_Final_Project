# Nicolas Seitz
# CSC1019

# ----------------------------------------
# Campus Event Planner: Main
# ----------------------------------------
# Imports all contents of the cal module into main
# This is the list where the event objects will be stored
events = []
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

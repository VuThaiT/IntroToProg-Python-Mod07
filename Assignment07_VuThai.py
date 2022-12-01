# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with Exception Handling and Pickle/Unpickle data.
# ChangeLog (Who,When,What):
# Vu Thai,11/29/2022,Created and Modified code to complete assignment 07
# ---------------------------------------------------------------------------- #

import pickle  #imports the pickle module

lstPickle = []
strFile = "ToDoList.dmp"

class IO:

    @staticmethod
    def output_menu_tasks():
        print('''
        +-------------------------------------------+
        Menu of Options:
        1) Add a new Task, Time, and Priority
        2) Unpickle Data File        
        3) Exit Program
        +-------------------------------------------+
        ''')
        print()  # Add an extra line for looks

    def input_menu_choice():
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

while (True):
    # Step 3 Show current data
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    if choice_str.strip() == '1':  # Add a new Task
        strTask = input("Please enter the name of the task: ")

        while (True):
            try:
                intTime = int(input("Please enter the number of hours needed for the task: "))
            except ValueError:
                print("Please use whole number integer only!")  # If anything other than an integer is returned print this message
                continue
            else:
                break

        while (True):
            lstCheck = ["low", "med", "high"] #create a list to force the user to input these 3 options only
            strPriority = input("Please enter the priority for this task (low | med | high): ").strip().lower()  # User only allow to input low, med, or high
            if strPriority.lower() in lstCheck:
                print()
            else:
                print("Please enter 'low', 'med', or 'high' only")
                continue
            break
        lstToDo = [strTask, intTime, strPriority]  # Task, time, and priority are placed into a list for pickling
        continue  # to show the menu

    elif choice_str == '2':  # Pickle and Unpickle data
        # Store inputs into a pickle dump file
        objFile = open(strFile, 'ab')  # Create file and opens it in append mode
        pickle.dump(lstToDo, objFile)  # Dump the list data to the file
        objFile.close()  # Close the file when done writing
        strUnPickle = input("\nPress any key to unpickle the data...\n")
        objFile = open(strFile, 'rb')  # Read the contents of the dump file
        while True:
            try:
                pklData = pickle.load(objFile)
                lstPickle.append(pklData)  # Append it to list
            except EOFError:
                break

        # Close the file
        objFile.close()
        print("[Task, Number of Hours, Priority]")

        # Traverse the data list, printing display
        for pklData in lstPickle:
            print(pklData)

        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        strExit = input("\nPress Enter to exit the script...\n")
        break  # to show the menu
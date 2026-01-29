"""
Daily Planner Assistant
by Man Ly 
"""

import os
import time

# Define color codes
RED = '\033[31m'
BOLD_RED = '\033[1;31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Difine style of text
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Set the invalid input of time and task message
invalid_time_input_message = RED + "\n---Please check your estimated time again!---\n"
invalid_time_input_message += "  It should not be negative numbers, zeros, or over 24 hours\n" + RESET
invalid_task_input_message = RED + "\n---Please check your name of task again!---\n"
invalid_task_input_message += "  It should not include numbers or symbols(expect space)\n" + RESET

def main():
    """Ask user information and then provide then a schedule suggestion"""
    user_todo_list = []
    again = "y"
        
    # Recall get_info() function to get and process information
    while again == "y":
        mini_list = get_info()

        # Append them into todo_list and ask user if they want to continue
        user_todo_list.append(mini_list)
        again = input(f" {BOLD}Do you want to conitune?(y/n): {RESET}")

    # Recall build_a_schedule() function to provide user a suggested schedule
    build_a_schedule(user_todo_list)
    print(f"\t{YELLOW}---Thank you for your time!---{RESET}")

def get_info():
    """Return 3 value that are processed from users input: name of task, estimated time, and suggested break"""
    # Set initial value to continue asking user if the time value is not valid
    invalid_time_input = True
    invalid_task_input = True

    # Ask user informations about task and time
    # If name of task input includes numbers or symbols (expect space),
    # Then, it will print a invalid task input message
    while invalid_task_input:
        task_input = input(f"What is your {BOLD}task{RESET} needed to be completed?: ")
        if " " in task_input:
            task_input_without_space = task_input.replace(" ", "")
            if task_input_without_space.isalpha():
                invalid_task_input = False
            else: 
                print(invalid_task_input_message)
                invalid_task_input = True
        else:
            if task_input.isalpha():
                invalid_task_input = False
            else: 
                print(invalid_task_input_message)
                invalid_task_input = True

    # If time input is a negative number, zero, or over 24 hours, it will ask user again and again
    while invalid_time_input:
        # Ask user if they want to enter time input in hour
        time_unit_check = input(f"{BOLD}Next, Do you want to {UNDERLINE}enter time input in hour{RESET}? (y/n): {RESET}")
        try:
            if time_unit_check == "y":
                time_input = float(input(f"What is your {BOLD}estimated time{RESET} for this task {BOLD}{UNDERLINE}(in hour){RESET}?: "))
                if time_input <= 0 or time_input >= 24:
                    print(invalid_time_input_message)
                    invalid_time_input = True
                else:
                    invalid_time_input = False
            elif time_unit_check == "n":
                time_input = float(input(f"What is your {BOLD}estimated time{RESET} for this task {BOLD}{UNDERLINE}(in minute){RESET}?: "))
                if time_input <= 0 or time_input >= 1440:
                    print(invalid_time_input_message)
                    invalid_time_input = True
                else:
                    invalid_time_input = False
            else:
                print(f"\t{RED}Error! Just use 'y' and 'n' please {RESET}")
        except ValueError:
            print(invalid_time_input_message.replace("negative numbers, zeros, or over 24 hours", "a string or symbols"))

    # Suggest a break based on valid time input (in hour)
    if invalid_task_input == False:
        if time_unit_check == "n":
            time_input = time_input / 60
        else: 
            time_input = time_input

        if time_input < 1:
            if time_input < 0.5: 
                break_amount = 5
            else:
                break_amount = 10
        else:
            break_amount = 15
        break_suggestion = BLUE + "---Take a " + str(break_amount) + "-minute break.---\n" + RESET
    print(break_suggestion)
    return task_input, time_input, break_suggestion, time_unit_check

def build_a_schedule(todo_list):
    """Build a schedule based on the valid values"""
    # Clear the screen to start the process
    os.system("cls")
    time.sleep(1)

    print("\tStarting Processing...")

    # Delay release of output (5 second at most)
    for i in range(6):
        print(i)
        time.sleep(0.5)

    # Add all the time values up in hours
    # if it is in minutes, convert it to hours and add it up (possibly round to the second decimal place.)
    os.system("cls")
    total_time = 0 
    for mini_list in todo_list:
        total_time += mini_list[1]      

    # If total of time values is greater than 24, it will print an invalid input message
    if total_time < 24:
        valid_value = True
        print(f" {GREEN} Your estimated time in total is: {str(round(total_time, 2))} hours {RESET}")

    else:
        valid_value = False
        print(f" {BOLD_RED} Your estimated time in total is: {str(total_time)} hours {RESET}")
        print(invalid_time_input_message)

    # If it doesn't, it will build a schedule
    if valid_value == True:
        print(f"\t {YELLOW}---Here's Your Schedule Suggestion!--- {RESET}")
        todo_list.sort(key = lambda time_value: time_value[1])
        for mini_list in todo_list:
            print("Your task is: ", mini_list[0])
            if mini_list[3] == "y":
                print(f"Task's estimated time is {mini_list[1]} hour(s)")
                print(mini_list[2].replace(".---", " each one hour.---"))
            else:
                print(f"Task's estimated time is {round(mini_list[1] * 60, 2)} minute(s)")
                print(mini_list[2])

main()



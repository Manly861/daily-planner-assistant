"""
Daily Planner Assistant
by Man Ly 
"""

def main():
    print("Welcome")

if __name__ == "__name__":
    main()
    
message = "---Please check your estimated time agian!---\n"
message += "It should not be negative numbers, zeros, or over 24 hours"

def main():
    user_todo_list = []
    again = "y"
    
    
    # Recall get_info() function to get information
    while again == "y":
        mini_list = get_info()

        # Add them into todo_list and ask user if they want to continue
        user_todo_list.append(mini_list)
        print(user_todo_list)
        again = input("Do you want to conitune?(y/n): ")

    # Recall build_a_schedule to provide user a suggested schedule\
    print("\tStarting Processing...")
    build_a_schedule(user_todo_list)

    print("\tThank you for your time!")

def get_info():
    """Return 3 value that are processed from users input: name of task, estimated time, and suggested break"""
    # Set initial value
    invalid_time = True

    # Ask user informations about task and time
    # If time value is a negative number, zero, or over 24 hours, keep asking user untill it is valid
    task = input("What is your task needed to be completed?: ")
    while invalid_time:
        time = float(input("What is your estimated time for this task (in hour)?: "))
        if time <= 0 or time >= 24:
            print(message)
            invalid_time = True
        else:
            invalid_time = False

    # Suggest a break based on valid time value
    if time <= 1:
        if time < 0.5: 
            break_amount = 5
        else:
            break_amount = 10
    else:
        break_amount = 15
    invalid_time = True
    break_suggestion = "---Take a " + str(break_amount) + "-minute break---"
    print(break_suggestion)

    return task, time, break_amount

def build_a_schedule(todo_list):
    """Build a schedule based on the valid values"""
    # Set initial value
    valid_value = True

    # Check if total of time values is greater than 24
    total_time = sum(mini_list[1] for mini_list in todo_list)
    print(f"Your estimated time in total is: " + str(total_time) + "hours")
    if total_time > 24:
        print(message)
        valid_value = False

    # Build a schedule based on these input
    if valid_value == True:
        todo_list.sort(key = lambda time_value: time_value[1])
        print(todo_list)
        for mini_list in todo_list:
            print("Your task is: ", mini_list[0])
            print("Task's estimated time (in hour) is ", mini_list[1])
            print("---Take a " + str(mini_list[2]) + " minute break---")
main()



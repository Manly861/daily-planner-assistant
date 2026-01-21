"""
Daily Planner Assistant
by Man Ly 
"""

def main():
    print("Welcome")

if __name__ == "__name__":
    main()

# Set the invalid input of time and task message
invalid_time_input_message = "\n---Please check your estimated time again!---\n"
invalid_time_input_message += "  It should not be negative numbers, zeros, or over 24 hours\n"
invalid_task_input_message = "\n---Please check your name of task again!---\n"
invalid_task_input_message += "  It should not include numbers or symbols\n"

def main():
    """Ask user information and then provide then a schedule suggestion"""
    user_todo_list = []
    again = "y"
        
    # Recall get_info() function to get information
    while again == "y":
        mini_list = get_info()

        # Append them into todo_list and ask user if they want to continue
        user_todo_list.append(mini_list)
        again = input("Do you want to conitune?(y/n): ")

    # Recall build_a_schedule() function to provide user a suggested schedule
    print("\tStarting Processing...")
    build_a_schedule(user_todo_list)
    print("\t   ---Thank you for your time!---")

def get_info():
    """Return 3 value that are processed from users input: name of task, estimated time, and suggested break"""
    # Set initial value to continue asking user if the time value is not valid
    invalid_time_input = True
    invalid_task_input = True

    # Ask user informations about task and time
    # If name of task input includes numbers or symbols, it will print a invalid task input message
    while invalid_task_input:
        task = input("What is your task needed to be completed?: ")
        if task.isalpha():
            invalid_task_input = False
        else: 
            print(invalid_task_input_message)
            invalid_task_input = True

    # If time input is a negative number, zero, or over 24 hours, it will ask user again and again
    while invalid_time_input:
        try:
            time = float(input("What is your estimated time for this task (in hour)?: "))
            if time <= 0 or time >= 24:
                print(invalid_time_input_message)
                invalid_time_input = True
            else:
                invalid_time_input = False
        except ValueError:
            print(invalid_time_input_message.replace("negative numbers, zeros, or over 24 hours", "a string or symbols"))

    # Suggest a break based on valid time value
    if invalid_task_input == False:
        if time <= 1:
            if time < 0.5: 
                break_amount = 5
            else:
                break_amount = 10
        else:
            break_amount = 15
    break_suggestion = "---Take a " + str(break_amount) + "-minute break---"
    print(break_suggestion)

    return task, time, break_amount

def build_a_schedule(todo_list):
    """Build a schedule based on the valid values"""
    # If total of time values is greater than 24, it will print an invalid input message 
    total_time = sum(mini_list[1] for mini_list in todo_list)
    print(f"Your estimated time in total is: " + str(total_time) + " hours")
    if total_time > 24:
        print(invalid_time_input_message)
        valid_value = False
    else:
        valid_value = True

    # If it doesn't, it will build a schedule
    print("\t---Here's Your Schedule Suggestion!---")
    if valid_value == True:
        todo_list.sort(key = lambda time_value: time_value[1])
        for mini_list in todo_list:
            print("Your task is: ", mini_list[0])
            print("Task's estimated time (in hour) is ", mini_list[1])
            print("---Take a " + str(mini_list[2]) + " minute break---")

main()



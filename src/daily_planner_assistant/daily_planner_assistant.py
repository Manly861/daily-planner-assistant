"""
Daily Planner Assistant
by Man Ly 
"""

def main():
    print("Welcome")

if __name__ == "__name__":
    main()


todo_list = []
again = "y"
valid_value = True
invalid_time = True

# Ask user informations about name of the tasks and estimated time for each one
# If time value is a negative number, zero, or over 24 hours, keep asking user untill it is valid
while again == "y":
    task = input("What is your task needed to be completed?: ")
    while invalid_time:
        time = float(input("What is your estimated time for this task (in hour)?: "))
        if time <= 0 or time >= 24:
            print("---Please check your estimated time agian!---")
            print("It should not be negative numbers, zeros, or over 24 hours" )
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

    # Add them into todo_list and ask user if they want to continue
    mini_list = [task, time, break_amount]
    todo_list.append(mini_list)
    print(todo_list)
    again = input("Do you want to conitune?(y/n): ")

# Check if total of time values is greater than 24
total_time = sum(mini_list[1] for mini_list in todo_list)
print(f"Your estimated time in total is: " + str(total_time) + "hours")
if total_time > 24:
    print("Please check your estimated time again! It should not be over limit time/n1")
    valid_value = False

# Build a schedule based on these input
if valid_value == True:
    todo_list.sort(key = lambda time_value: time_value[1])
    print(todo_list)
    for mini_list in todo_list:
        print("Your task is: ", mini_list[0])
        print("Task's estimated time (in hour) is ", mini_list[1])
        print("---Take a " + str(mini_list[2]) + " minute break---")

print("Thank you for your time!")







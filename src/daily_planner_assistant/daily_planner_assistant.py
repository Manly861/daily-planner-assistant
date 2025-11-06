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

# Ask user some information
while again == "y":
    task = input("What is your task needed to be completed?: ")
    time = float(
        input("What is your estimated time for this task (in hour)?: ")
        )

    # Check the time value if it is valid and then suggest a break
    if time <= 0 or time >= 24:
        print("---Please check your estimated time agian!---")
        print("It may be over 24 hours or a negative number" )
        time = float(
            input("What is your estimated time for this task (in hour)?: ")
        )
    elif time <= 1:
        if time < 0.5: 
            break_amount = 5
        else:
            break_amount = 10
    else:
        break_amount = 15
    break_suggestion = "---Take a " + str(break_amount) + "-minute break---"
    print(break_suggestion)

    # Add them into todo_list and ask user if they want to continue
    mini_list = [task, time, break_amount]
    todo_list.append(mini_list)
    print(todo_list)
    again = input("Do you want to conitune?(y/n): ")

# Check if total of time values is greater than 24
total_time = sum(mini_list[1] for mini_list in todo_list)
print(total_time)








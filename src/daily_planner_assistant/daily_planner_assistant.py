"""
Daily Planner Assistant
by Man Ly 
"""

def main():
    print("Welcome")

if __name__ == "__name__":
    main()


 
again = "yes"

# Ask user some information
while again == "yes":
    task = input("What is your task needed to be completed?: ")
    time = float(
        input("What is your estimated time for this task (in hour)?: ")
        )

    # Check the time value if it is valid and then suggest a break
    if time <= 0 or time >= 24:
        print("Please check your estimated time agian!")
        print("It may be over 24 hours or a negative number" )
        continue 
    elif time < 1:
        if time < 0.5: 
            break_amount = 5
        else:
            break_amount = 10
    else:
        break_amount = 15
    break_suggestion = "Take a " + str(break_amount) + "-minute break"
    print(break_suggestion)
    again = "no"

# Add them into todo_list and ask user if they want to continue
# Check if total of time values is greater than 24




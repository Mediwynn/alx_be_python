reminder = input("Enter your reminder: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")



match priority:
    case 'high':
        print( "Reminder: ", reminder, "is a high priority reminder", end= " ")

    case 'medium':
        print( "Memo: ", reminder, "is a medium priority reminder", end= " ")

    case 'low':
        print( "Note: ", reminder, "is a low priority reminder", end= " ")

    case _:
        print("Invalid priority level")

if time_bound == "yes":
    print("that requires immediate attention today!")

else:
    print("Consider completing it when you have free time.")
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")



match priority:
    case 'high':
        print("Reminder: ", task, "is a high priority task", end= " ")

    case 'medium':
        print("Reminder: ", task, "is a medium priority task", end= " ")

    case 'low':
        print("Reminder: ", task, "is a low priority task", end= " ")

    case _:
        print("Invalid priority level")

if time_bound == "yes":
    print("that requires immediate attention today!")

else:
    print("Consider completing it when you have free time.")
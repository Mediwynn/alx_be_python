task = input("Enter your task: ")
prio = input("Priority (high/medium/low): ")
times_sensitive = input("Is it time-bound? (yes/no): ")



match prio:
    case 'high':
        print("Reminder: ", task, "is a high priority task", end= " ")

    case 'medium':
        print("Memo: ", task, "is a medium priority task", end= " ")

    case 'low':
        print("Note: ", task, "is a low priority task", end= " ")

    case _:
        print("Invalid priority level")

if times_sensitive == "yes":
    print("that requires immediate attention today!")

else:
    print("Consider completing it when you have free time.")
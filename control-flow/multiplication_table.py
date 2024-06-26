userin = int(input("Enter a number to see its multiplication table: "))
i = 1

for i in range(1, 11):
    result = userin * i
    print(userin, "*", i, "=", result)
    i = i + 1

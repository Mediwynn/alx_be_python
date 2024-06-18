income =  int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = income - expenses
rate = 0.05

projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

print("Your monthly monthly_savings are ", monthly_savings)
print("Projected monthly_savings after one year, with interest, is: ", projected_savings)

monthly_income =  int(input("Enter your monthly monthly_income: "))
monthly_expenses = int(input("Enter your total monthly monthly_expenses: "))

monthly_savings = monthly_income - monthly_expenses
rate = 0.05

projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

print("Your monthly monthly_savings are ", monthly_savings)
print("Projected monthly_savings after one year, with interest, is: ", projected_savings)

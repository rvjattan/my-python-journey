# return in python has two function, exiting a function and passing a value back to the caller

def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate  #returns the calculated value to the caller

new_zealand_exchange = calculate_exchange_usd(100, 1.4)

print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")

# output: 100 dollars in US currency would give you 140 New Zealand dollars

# Example >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

current_budget = 3500.75
shirt_expense = 9

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

def deduct_expense(budget, expense):
  return budget - expense

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)
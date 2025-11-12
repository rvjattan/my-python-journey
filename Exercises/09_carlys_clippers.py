hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Step 1: create a new variable total_price so that it can contain sum of all haircut prices
total_price = 0

# Step 2: loop through prices list and add each price to total_price
for price in prices:
  total_price += price

# Step 3: calculate the average price and store it in a new variable average_price:
average_price = total_price / len(prices)

# Step 4: Print average_price
print("Average Haircut Price: $", average_price)

# Step 5: create a new price list with each price element reduced by 5; use list comprehension method:
new_prices = [price - 5 for price in prices]

# Step 6: print new_prices
print(new_prices)

# Step 7: Create a new variable total_revenue that can hold the revenue value
total_revenue = 0

# Step 8 & 9: add a for loop to create a variable i that goes from 0 to len(hairstyles) and add the prices[i] and last_week[i] to total_revenue :
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

# Step 10: print total_revenue
print(total_revenue)

# Step 11: find average_daily_revenue & print it out
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Step 12: create a list for cuts_under_30 :
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

# print cuts_under_30
print(cuts_under_30)
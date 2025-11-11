# step 1: create a list called toppings:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# step 2: create a list called prices:
prices = [2, 6, 1, 3, 2, 7, 2]

# step 3: count the occurrences of $2 slices and print it out:
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# step 4: find length of the toppings list and store it in a new variable:
num_pizzas = len(toppings)

# step 5: print the string We sell [num_pizzas] different kinds of pizza!, where [num_pizzas] represents the value of our variable num_pizzas
print(f"We sell {num_pizzas} different kinds of pizza!")

# step 6: using the toppings and prices details create a new 2d list called pizza_and_prices:
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

# step 7: print pizza_and_prices list:
print(pizza_and_prices)

# step 8: sort pizza_and_prices in ascending price order:
pizza_and_prices.sort()

# step 9: store first element of pizza_and_prices to a new variable cheapest_pizza
cheapest_pizza = pizza_and_prices[0]

# step 10: store last element of pizza_and_prices to a new variable priciest_pizza
priciest_pizza = pizza_and_prices[-1]

# step 11: remove the last element ie priciest_pizza from the pizza_and_prices list:
pizza_and_prices.pop()

# step 12: add new pizza toping to the list according to the price:
pizza_and_prices.insert(4, [2.5, "peppers"])

# step 13: store 3 cheapest pizzas to a variable three_cheapest:
three_cheapest = pizza_and_prices[0:3]

# step 14: print three_cheapest list:
print(three_cheapest)
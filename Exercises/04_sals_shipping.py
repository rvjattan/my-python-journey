# A python program that takes the weight of the package and then calculates which method of shipping is cheapest and tells the shipping price

  # Step 1: define a "weight" variable and set it to a number:
weight = 8.4

#Step 2: calculate cost for ground shipping

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

#Step 3: print cost for 8.4 lb package
print("Ground Shipping Charges: $" + str(cost_ground))

#Step 4: variable for premium ground shipping:
premium_shipping_charges = 125

#Step 5: calculating cost for premium ground shipping
print("Ground Shipping (Premium): $" + str(premium_shipping_charges))

#Step 6: calculate drone shipping cost

weight = 1.5

if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9
elif weight <= 10:
  cost_drone = weight * 12
else:
  cost_drone = weight * 14.25

#Step 7: print drone shipping cost
print("Drone Shipping Charges: $" + str(cost_drone))


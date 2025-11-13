# Function parameters allows the function to accept data as parameter value.
# Parameter value is written between the parenthesis() of a function.

def trip_welcome_sign(destination):
  print("Welcome to Vacation House") 
  print("Looks like you're going to " + destination + " today.")

# now call the function with parameter value
trip_welcome_sign("Thailand")

# Example >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)

generate_trip_instructions("Grand Central Station") # calls the function with parameter value

# >>>>>>>>>>>>>>>  Multiple Parameters  >>>>>>>>>>>>>>>>>>>>

# a function can have multiple parameters seperated by comma(,)

def trip_welcome(origin, destination):
  print("Welcome to Vacation House")
  print("Looks like you are traveling from " + origin)
  print("And you are heading to " + destination)

trip_welcome("Dubai", "Tokyo")

# Example >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  
  car_rental_total = car_rental_rate * trip_time

  hotel_total = hotel_rate * trip_time - 10 # 10 is discount

  trip_total = car_rental_total + hotel_total + plane_ticket_price

  return trip_total

# Step 5: call your function

print(calculate_expenses(200, 100, 100, 5))
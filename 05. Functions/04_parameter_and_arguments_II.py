# there are 3 types of arguments that can be given to a function:

# (i) Positional Arguments:

def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )

# (ii) Keyword Arguments: where we explicitly refers to what each argument is assigned to in the function call.

calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100) # here function is called

# (iii) Default Arguments: arguments that are given a default value / we can also provide an overwrite value
 
def calculate_taxi_price(miles_to_travel, rate, discount = 10): # discount has a default value of 10
  print(miles_to_travel * rate - discount )
                  

# Example >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def trip_planner(first_destination, second_destination, final_destination="Japan"):
  print("Here is what your trip will look like!")
  print("First, we will stop in", first_destination, "then", second_destination, "and lastly", final_destination)

trip_planner("France", "Germany", "Denmark")
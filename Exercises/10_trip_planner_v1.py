# A program that displays origin, destination, time and mode of transport for the trip

# Welcomes the user
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0", name)

# Rounds off the time:
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(2.5)

# Structure of the output
def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in", origin)
  print("And you are travelling to", destination)
  print("You will be traveling by", mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")

destination_setup("Tokyo", "San Jose", estimate, "Plane")
# Functions are reusable blocks of code designed to perform a specific, well designed task.
# Fuctions make code easier to manage, debug and allow code reuse.

# Structure: 
#   def function_name():        (def indicates the begining, fun name is followed by parenthesis() and colon:
#        functions tasks go here        (indented)

# Example:

def trip_welcome():
  print("Welcome to Vacation House!") 
  print("Let's get you to your destination.")

# the above print prints nothing because the function has not been called

# >>>>>>>>>>>>>>>>>>>>>    Calling a function          >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# to call a function we need to type out the function name including parenthesis:

def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")

directions_to_timesSq()     # calling the function, this prints out the above 3 print statements


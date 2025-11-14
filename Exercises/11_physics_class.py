train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# step 1: write function to convert fahrenheit to celsius:
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# step 2: convert fahrenheit to celsius
f100_in_celsius = f_to_c(100)

# step 3: write function to convert celsius to fahrenheit:
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

# step 4: convert celsius to fahrenheit
c0_in_fahrenheit = c_to_f(0)

# step 5: write a function that takes mass and acceleration and returns mass * acceleration:
def get_force(mass, acceleration):
  return mass * acceleration

# step 6: test the get_force function:
train_force = get_force(train_mass, train_acceleration)

# step 7: print the string:
print("The GE train supplies", train_force, "Newtons of force.")

# step 8: create a function that takes mass and c:
def get_energy(mass, c=3*10**8):
  return mass * (c ** 2)

# step 9: test get_energy:
bomb_energy = get_energy(bomb_mass)

# step 10: print string:
print("A 1kg bomb supplies", bomb_energy, "Joules")

# step 11: create function get_work that takes mass, acceleration and distance:
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

# step 12: test get_work:
train_work = get_work(train_mass, train_acceleration, train_distance)

# step 13: print the string:
print("The GE train does", train_work, "Joules of work over", train_distance, "meters.")
# Example:

project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

# Loop through each sublist
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)          # print individual student


# Example:

# ice-cream scoops sold in various locations, find out the total scoops sold

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  print(location)  # prints three lists: [12, 17, 22], [2, 10, 3], [5, 12, 13]
  for i in location: # iterate through every list
    scoops_sold += i # add i to scoops sold

print(scoops_sold) # prints the sum of total scoops 
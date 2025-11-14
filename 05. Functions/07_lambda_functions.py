# lambda functions are small anonymous functions that can have any number of arguments but only one expression.
# defined using "lambda" keyword; used for short and simple operations

# syntax:

lambda [arguments]: [expression] 

# regular function: 

def square(x): 
    return x ** 2 

# lamda function:

square_lambda = lambda x: x ** 2


greeting = lambda name: f"Hello, {name}!" 
print(greeting("Alice"))  # Output: Hello, Alice! 

# lambda functions are used as arguments to higher order functions such as map(), filter() and sorted()
# Higher functions are functions that can accept other functions as arguments

# (i) map()
numbers = [1, 2, 3, 4, 5] 
squared = list(map(lambda x: x ** 2, numbers)) 
print(squared)  # Output: [1, 4, 9, 16, 25] 

# (ii) filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) 
print(even_numbers)  # Output: [2, 4, 6, 8, 10] 

# (iii) sorted()
students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)] 
sorted_students = sorted(students, key=lambda x: x[2]) 
print(sorted_students) 

# Output: [('Bob', 'B', 12), ('Alice', 'A', 15), ('Charlie', 'A', 20)]
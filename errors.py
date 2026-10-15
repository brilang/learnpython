x = 42
y = 0

try:
    print(x/y)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
else:
    print("Something went wrong.")
finally:
    print("Execution completed.")
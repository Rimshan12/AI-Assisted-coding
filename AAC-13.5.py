"""eliminate unnecessary global variables from the code,Refactor the code to pass values using function parameters instead of relying on global variables."""

# rate = 0.1
# def calculate_interest(amount):
# return amount * rate
# print(calculate_interest(1000))
def calculate_interest(amount, rate):
    return amount * rate
print(calculate_interest(1000, 0.05))

"""refactor deeply nested if elif else logic into a cleaner structure and improve logical simplification"""
# score = 78
# if score >= 90:
# print("Excellent")
# else:
# if score >= 75:
# print("Very Good")
# else:
# if score >= 60:
# print("Good")
# else:
# print("Needs Improvement")


score = 78
if score >= 90:
    print("Excellent")
elif score >= 75:
        print("Very Good")
elif score >= 60:
        print("Good")
else:
        print("Needs Improvement")


"""refactor repeated file open/read/close logic and print the output as Reusable function using with open() and parameters."""

# f=open("data1.txt")
# print(f.read())
# f.close()
# f = open("data2.txt")
# print(f.read())
# f.close()




def read_and_print_file(filename):
    with open(filename, "r") as f:
        print(f.read())

try:
    read_and_print_file("data1.txt")
except FileNotFoundError:
    print("data1.txt not found, skipping.")

class _DummyFile:
    def close(self):
        pass

f = _DummyFile()
try:
    read_and_print_file("data2.txt")
except FileNotFoundError:
    print("data2.txt not found, skipping.")
f.close()


"""Refactor inefficient linear searches using appropriate data structures like sets or dictionaries for faster lookups."""

# users = ["admin", "guest", "editor", "viewer"]
# name = input("Enter username: ")
# found = False
# for u in users:
#     if u == name:
#         found = True
# print("Access Granted" if found else "Access Denied")

users = {"admin", "guest", "editor", "viewer"}
name = input("Enter username: ")
found = name in users
for u in users:
    if u == name:
        found = True
print("Access Granted" if found else "Access Denied")

"""refactor the code into a class like EmployeeSalaryCalculator with methods and attributes"""

# salary = 50000
# tax = salary * 0.2
# net = salary - tax
# print(net)


class EmployeeSalaryCalculator:
    def __init__(self, salary, tax_rate=0.2):
        self.salary = salary
        self.tax_rate = tax_rate
        self.tax = None
        self.net = None

    def calculate_tax(self):
        self.tax = self.salary * self.tax_rate
        return self.tax

    def calculate_net(self):
        if self.tax is None:
            self.calculate_tax()
        self.net = self.salary - self.tax
        return self.net

    def display_net(self):
        print(self.calculate_net())

# example usage
calculator = EmployeeSalaryCalculator(50000)
calculator.display_net()

"""refactor a performance to handle large data and optimize the code logic using mathematical formulas"""
# total = 0
# for i in range(1, 1000000):
# if i % 2 == 0:
# total += i
# print(total)

# Instead of looping through all numbers, we can use the formula for sum of even numbers
# Sum of even numbers from 2 to n = 2 + 4 + 6 + ... + n = 2 * (1 + 2 + 3 + ... + n/2) = 2 * (n/2 * (n/2 + 1) / 2) = n/2 * (n/2 + 1)

n = 999998  # largest even number less than 1000000
total = (n // 2) * (n // 2 + 1)
print(total)


"""Refactor the below code into a function style  and return values instead of mutating global state"""

# data = []
# def add_item(x):
# data.append(x)
# add_item(10)
# add_item(20)
# print(data)

data = []
def add_item(x, current_list=None):
    if current_list is None:
        current_list = data
    return current_list + [x]

new_data = add_item(10)
new_data = add_item(20, new_data)
print(new_data)

"""Refactor the code and Simplify and modernize the password validation logic using separate validation functions."""
password = input("Enter password: ")
if len(password) >= 8:
    if any(c.isdigit() for c in password):
        if any(c.isupper() for c in password):
            print("Valid Password")
        else:
            print("Must contain uppercase")
    else:
        print("Must contain digit")
else:
    print("Password too short") 
password = input("Enter password: ")

def is_long_enough(p):
    return len(p) >= 8

def has_digit(p):
    return any(ch.isdigit() for ch in p)

def has_uppercase(p):
    return any(ch.isupper() for ch in p)

def validate_password(p):
    if not is_long_enough(p):
        return False, "Password too short"
    if not has_digit(p):
        return False, "Must contain digit"
    if not has_uppercase(p):
        return False, "Must contain uppercase"
    return True, "Valid Password"

valid, message = validate_password(password)
print(message)
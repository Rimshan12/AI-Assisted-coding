"""Refactored code with a reusable function and no duplication"""

# print("Area of Rectangle:", 5 * 10)
# print("Perimeter of Rectangle:", 2 * (5 + 10))

# print("Area of Rectangle:", 7 * 12)
# print("Perimeter of Rectangle:", 2 * (7 + 12))

# print("Area of Rectangle:", 10 * 15)
# print("Perimeter of Rectangle:", 2 * (10 + 15))

def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Area of Rectangle: {area}")
    print(f"Perimeter of Rectangle: {perimeter}")

calculate_rectangle_properties(5, 10)
calculate_rectangle_properties(7, 12)

print("Area of Rectangle:", 10 * 15)
print("Perimeter of Rectangle:", 2 * (10 + 15))


"""Refactor the Code with a function calculate_total(price) that can be reused for multiple price inputs."""
# price = 250
# tax = price * 0.18
# total = price + tax
# print("Total Price:", total)

# price = 500
# tax = price * 0.18
# total = price + tax
# print("Total Price:", total)



def calculate_total(price):
    tax = price * 0.18
    tax = price * 0.18
    total = price + tax
    print("Total Price:", total)

calculate_total(250)
calculate_total(500)

"""Refactor the code and define a class Gradecalculator with a method calculate_grade(marks) that can be reused for different marks inputs and returns the grade instead of printing it directly."""

# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# else:
#     print("Grade C")
# marks = 72
# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# else:
#     print("Grade C")

class GradeCalculator:
    def calculate_grade(self, marks):
        if marks >= 90:
            return "Grade A"
        elif marks >= 75:
            return "Grade B"
        else:
            return "Grade C"
grade_calculator = GradeCalculator()
print(grade_calculator.calculate_grade(95))
print(grade_calculator.calculate_grade(80))
print(grade_calculator.calculate_grade(72))

"""Refactor code and add functions like get_input(), calculate_square(), and display_result()"""

# num = int(input("Enter number: "))
# square = num * num
# print("Square:", square)

def get_input():
    return int(input("Enter a number: "))

def calculate_square(number):
    return number * number

def display_result(number, square):
    print(f'Square of {number} is {square}')

number = get_input()
square = calculate_square(number)
display_result(number, square)

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

"""refactor the code into a proper format with functions like add_book(), search_book(), and remove_book() to manage the library database effectively."""
library_db = {}

def add_book(title, author, isbn):
    if isbn not in library_db:
        library_db[isbn] = {"title": title, "author": author}
        print("Book added successfully.")
    else:
        print("Book already exists.")

def search_book(isbn):
    if isbn in library_db:
        print("Book Found:", library_db[isbn])
    else:
        print("Book not found.")

def remove_book(isbn):
    if isbn in library_db:
        del library_db[isbn]
        print("Book removed successfully.")
    else:
        print("Book not found.")

# Adding first book
title = "Python Basics"
author = "John Doe"
isbn = "101"

add_book(title, author, isbn)

# Adding second book (duplicate logic)
title = "AI Fundamentals"
author = "Jane Smith"
isbn = "102"

add_book(title, author, isbn)

# Searching book (repeated logic structure)
search_book("101")

# Removing book (again repeated pattern)
remove_book("101")

# Searching again
search_book("101")

if isbn not in library_db:
    library_db[isbn] = {"title": title, "author": author}
    print("Book added successfully.")
else:
    print("Book already exists.")

# Adding second book (duplicate logic)
title = "AI Fundamentals"
author = "Jane Smith"
isbn = "102"

if isbn not in library_db:
    library_db[isbn] = {"title": title, "author": author}
    print("Book added successfully.")
else:
    print("Book already exists.")

# Searching book (repeated logic structure)
isbn = "101"
if isbn in library_db:
    print("Book Found:", library_db[isbn])
else:
    print("Book not found.")

# Removing book (again repeated pattern)
isbn = "101"
if isbn in library_db:
    del library_db[isbn]
    print("Book removed successfully.")
else:
    print("Book not found.")

# Searching again
isbn = "101"
if isbn in library_db:
    print("Book Found:", library_db[isbn])
else:
    print("Book not found.")

"""Refactor into a clean reusable function (generate_fibonacci ) add test cases"""

def generate_fibonacci(n):
    a, b = 0, 1
    print(a)
    print(b)
    for i in range(2,n):
        c = a + b
        print(c)
        a, b = b, c
n = int(input("Enter limit: "))
generate_fibonacci(n)   
# Test case 1: n = 0
print("Test case 1: n = 0")
generate_fibonacci(0)

# Test case 2: n = 1
print("Test case 2: n = 1")
generate_fibonacci(1)

# Test case 3: n = 2
print("Test case 3: n = 2")
generate_fibonacci(2)

# Test case 4: n = 5
print("Test case 4: n = 5")
generate_fibonacci(5)

# n=int(input("Enter limit: "))
# a=0
# b=1
# print(a)
# print(b)
# for i in range(2,n):
#  c=a+b
#  print(c)
#  a=b
#  b=c

"""Refactor the code into is_prime(n) and is_twin_prime(p1, p2) and generate list of twin primes"""
# a=11
# b=13
# fa=0
# for i in range(2,a):
#  if a%i==0:
#   fa=1
# fb=0
# for i in range(2,b):
#  if b%i==0:
#   fb=1
# if fa==0 and fb==0 and abs(a-b)==2:
#  print("Twin Primes")
# else:
#  print("Not Twin Primes")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_twin_prime(p1, p2):
    return is_prime(p1) and is_prime(p2) and abs(p1 - p2) == 2
twin_primes = []
for num in range(2, 100):
    if is_prime(num) and is_twin_prime(num, num + 2):
        twin_primes.append((num, num + 2))
print("Twin Primes:", twin_primes)

"""Refactor the code to determine the Chinese Zodiac sign based on the year input using function get_zodiac(year) and return the zodiac sign instead of printing it directly."""
def get_zodiac(year):
    zodiac_signs = [
        "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox",
        "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat"
    ]
    return zodiac_signs[year % 12]
year = int(input("Enter year: "))
zodiac_sign = get_zodiac(year)
print(f"The Chinese Zodiac sign for the year {year} is: {zodiac_sign}")


""" Refactor the code to check if a number is a Harshad number using a function is_harshad(number)accepts  only integers that returns True or False instead of printing the result directly."""
# num = int(input("Enter a number: "))
# temp = num
# sum_of_digits = 0
# while temp > 0:
#     digit = temp % 10
#     sum_of_digits += digit
#     temp //= 10
# if num % sum_of_digits == 0:
#     print(f"{num} is a Harshad number.")
# else:
#     print(f"{num} is not a Harshad number.")
def is_harshad(number):
    temp = number
    sum_of_digits = 0
    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit
        temp //= 10
    return number % sum_of_digits == 0
num = int(input("Enter a number: "))
if is_harshad(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")

""""Refactor the given poorly structured Python script into a clean and reusable function that calculates the factorial of a number and counts the trailing zeros in the factorial result."""
# n = int(input("Enter a number: "))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(f"Factorial of {n} is {fact}")
# count = 0
# while fact % 10 == 0:
#     count += 1
#     fact //= 10
# print(f"Number of trailing zeros in {n}! is {count}")
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
def count_trailing_zeros(n):
    count = 0
    while n % 10 == 0:
        count += 1
        n //= 10
    return count
n = int(input("Enter a number: "))
fact = factorial(n)
print(f"Factorial of {n} is {fact}")
trailing_zeros = count_trailing_zeros(fact)
print(f"Number of trailing zeros in {n}! is {trailing_zeros}")

""" generate a python code for  Collatz Sequence Generator  with test cases"""
def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence
# Test cases
print("Test case 1: n = 6")
print(collatz_sequence(6)) 
print("Test case 2: n = 19")
print(collatz_sequence(19))  
print("Test case 3: n = 1")
print(collatz_sequence(1))

""" Generate a python code for Lucas sequence up to n terms and add test cases"""
def lucas_sequence(n):
    sequence = []
    a, b = 2, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
# Test cases
print("Test case 1: n = 0")
print(lucas_sequence(5))
print("Test case 2: n = 1")
print(lucas_sequence(1))
print("Test case 3: n = 10")
print(lucas_sequence(10))

"""Generate a python code for Count vowels and consonants in string. Add test cases"""
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

# Test cases
print("Test case 1: 'Hello World'")
v, c = count_vowels_consonants("Hello World")
print(f"Vowels: {v}, Consonants: {c}")

print("Test case 2: 'Programming'")
v, c = count_vowels_consonants("Programming")
print(f"Vowels: {v}, Consonants: {c}")

print("Test case 3: 'AEIOU'")
v, c = count_vowels_consonants("AEIOU")
print(f"Vowels: {v}, Consonants: {c}")


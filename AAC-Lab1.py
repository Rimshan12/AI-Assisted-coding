def is_palindrome(s):
    """Check if a string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Test examples
print(is_palindrome("racecar"))      # True
print(is_palindrome("hello"))        # False
print(is_palindrome("A man a plan a canal Panama"))  # True




def sum_two_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

# Test examples
print(sum_two_numbers(5, 3))        # 8
print(sum_two_numbers(10, -4))      # 6
print(sum_two_numbers(2.5, 1.5))    # 4.0


def multiplication_table_reverse(n):
    """Generate multiplication table from n down to 1."""
    for i in range(n, 0, -1):
        print(f"{i} x 5 = {i * 5}")

# Test example
multiplication_table_reverse(100)

def countdown_by_twenties(start):
    """Generate numbers from start down to 1, printing every 20th multiple."""
    for i in range(start, 0, -20):
        print(i)

# Test example
countdown_by_twenties(100)

def multiplication_tables_reverse(limit):
    """Generate multiplication tables from limit down to 1, each with 20 multiples in reverse."""
    for num in range(limit, 0, -1):
        print(f"\nMultiplication table of {num}:")
        for multiple in range(1,21):
            print(f"{num} x {multiple} = {num * multiple}")

# Test example
multiplication_tables_reverse(100)
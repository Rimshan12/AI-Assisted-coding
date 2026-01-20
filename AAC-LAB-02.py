def sum_even_odd(numbers):
    sum_even = sum(num for num in numbers if num % 2 == 0)
    sum_odd = sum(num for num in numbers if num % 2 != 0)
    return sum_even, sum_odd

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum, odd_sum = sum_even_odd(numbers)

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")

"""Module for calculating sums of even and odd numbers."""

def calculate_even_odd_sums(numbers: list[int]) -> tuple[int, int]:
    """
    Calculate the sum of even and odd numbers in a list.
    
    Args:
        numbers: List of integers to process.
        
    Returns:
        Tuple containing (sum_of_even, sum_of_odd).
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    
    return even_sum, odd_sum

def main() -> None:
    """Main entry point for the program."""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    even_sum, odd_sum = calculate_even_odd_sums(numbers)
    
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")

if __name__ == "__main__":
    main()

import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

# Example usage:
if __name__ == "__main__":
    print("Area of Circle (radius=5):", area_circle(5))
    print("Area of Rectangle (length=4, width=6):", area_rectangle(4, 6))
    print("Area of Triangle (base=3, height=4):", area_triangle(3, 4))

def is_prime(n):
    """Check whether a number is prime or not."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Get input from user
num = int(input("Enter a number: "))

# Check and display result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

def is_prime(n):
    """
    Check if a number is prime with O(√n) time complexity.
    
    Args:
        n: Integer to check
        
    Returns:
        Boolean: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to √n
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    
    return True

# Test cases
if __name__ == "__main__":
    test_numbers = [1, 2, 17, 20, 97, 100, 541]
    
    for num in test_numbers:
        result = is_prime(num)
        print(f"{num} is {'prime' if result else 'not prime'}")

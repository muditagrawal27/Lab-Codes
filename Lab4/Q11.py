def factorial(n):
    """Calculate the factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def calculate_sin(x, terms=10):
    """Calculate sin(x) using the series expansion."""
    result = 0
    for i in range(terms):
        sign = (-1)**i
        power = 2*i + 1
        result += ((x**power) / factorial(power)) * sign
    return result

# Example usage
pi = 3.14159
x_in_degrees = 60  # Convert to radians
x_in_radians = pi / 180 * x_in_degrees
sin_x = calculate_sin(x_in_radians)
print(f"sin({x_in_degrees} degrees) ≈ {sin_x}")

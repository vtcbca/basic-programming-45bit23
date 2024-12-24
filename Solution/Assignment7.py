def number_triangle_simple(n):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")  # Leading spaces
        for j in range(1, 2 * i):
            print(j, end=" ")  # Print numbers
        print()

# Example usage
num_lines = int(input("Enter the number of lines: "))
number_triangle_simple(num_lines)

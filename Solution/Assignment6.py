def star_pattern_loop(n):
    for i in range(1, n + 1):
        print('* ' * i)

# Example usage
num_rows = int(input("Enter the number of rows: "))
star_pattern_loop(num_rows)

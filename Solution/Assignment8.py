def alphabet_pattern_simple(n):
    for i in range(1, n + 1):
        # Print leading spaces for alignment
        print(" " * (n - i), end="")
        
        # Print the first half of the alphabet
        for j in range(1, i + 1):
            print(chr(64 + j), end=" ")
        
        # Print the second half of the alphabet (reverse)
        for j in range(i - 1, 0, -1):
            print(chr(64 + j), end=" ")
        
        print()

# Example usage
num_lines = int(input("Enter the number of lines: "))
alphabet_pattern_simple(num_lines)

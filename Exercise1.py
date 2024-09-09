def letter_to_number(s):
    # Convert each letter to its corresponding number (a=1, b=2, ..., z=26)
    s = s.lower()  # Convert to lowercase to handle uppercase inputs
    total_sum = sum(ord(char) - ord('a') + 1 for char in s if char.isalpha())
    
    # Reduce to a single digit
    while total_sum >= 10:
        total_sum = sum(int(digit) for digit in str(total_sum))
    
    return total_sum

# Example usage
s = "abcde"
result = letter_to_number(s)
print(result)

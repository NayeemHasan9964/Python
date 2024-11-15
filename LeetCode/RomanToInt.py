def romanToInt(s: str) -> int:
    # Define a dictionary to map Roman numerals to integers
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    # Iterate through the Roman numeral string in reverse
    for char in reversed(s):
        current_value = roman_to_int[char]

        # If the current value is less than the previous value, subtract it; otherwise, add it
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        # Update the previous value for the next iteration
        prev_value = current_value

    return total


# Example usage
print(romanToInt("III"))  # Output: 3
print(romanToInt("IV"))  # Output: 4
print(romanToInt("IX"))  # Output: 9
print(romanToInt("LVIII"))  # Output: 58
print(romanToInt("MCMXCIV"))  # Output: 1994



